const { Plugin, Notice } = require("obsidian");
const { execFile } = require("child_process");

const DEFAULT_SETTINGS = {
  dockerContainer: "mggrafeno-postgres",
  database: "MG-Grafeno-Local",
  user: "postgres",
  timeoutMs: 15000,
};

module.exports = class MgGrafenoQueryPlugin extends Plugin {
  async onload() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());

    this.registerMarkdownCodeBlockProcessor("mg-grafeno-sql", async (source, el) => {
      await this.renderQuery(source, el);
    });

    this.addCommand({
      id: "mg-grafeno-query-test",
      name: "Testar conexao com mg-grafeno",
      callback: async () => {
        try {
          await this.runSql("select current_database() as database, now() as checked_at;");
          new Notice("MG Grafeno Query: conexao OK.");
        } catch (error) {
          new Notice(`MG Grafeno Query: ${error.message}`);
        }
      },
    });
  }

  async renderQuery(source, el) {
    el.empty();
    el.addClass("mg-grafeno-query");

    const sql = source.trim();
    if (!sql) {
      el.createEl("div", { cls: "mg-grafeno-query__error", text: "Consulta vazia." });
      return;
    }

    if (!this.isReadOnly(sql)) {
      el.createEl("div", {
        cls: "mg-grafeno-query__error",
        text: "Consulta bloqueada: use apenas SELECT ou WITH.",
      });
      return;
    }

    const status = el.createEl("div", {
      cls: "mg-grafeno-query__status",
      text: "Consultando mg-grafeno...",
    });

    try {
      const csv = await this.runSql(sql);
      status.remove();
      this.renderCsv(csv, el);
    } catch (error) {
      status.remove();
      el.createEl("div", { cls: "mg-grafeno-query__error", text: error.message });
    }
  }

  isReadOnly(sql) {
    const normalized = sql
      .replace(/\/\*[\s\S]*?\*\//g, "")
      .replace(/--.*$/gm, "")
      .trim()
      .toLowerCase();

    if (!/^(select|with)\b/.test(normalized)) return false;

    const blocked = /\b(insert|update|delete|drop|alter|create|truncate|grant|revoke|copy|call|do|merge|vacuum|analyze|refresh|reindex)\b/;
    return !blocked.test(normalized);
  }

  runSql(sql) {
    return new Promise((resolve, reject) => {
      const args = [
        "exec",
        this.settings.dockerContainer,
        "psql",
        "-U",
        this.settings.user,
        "-d",
        this.settings.database,
        "--csv",
        "-v",
        "ON_ERROR_STOP=1",
        "-c",
        sql,
      ];

      execFile("docker", args, { timeout: this.settings.timeoutMs }, (error, stdout, stderr) => {
        if (error) {
          const detail = (stderr || error.message || "Falha ao executar consulta.").trim();
          reject(new Error(detail));
          return;
        }
        resolve(stdout.trim());
      });
    });
  }

  renderCsv(csv, el) {
    if (!csv) {
      el.createEl("div", { cls: "mg-grafeno-query__empty", text: "Consulta sem resultado." });
      return;
    }

    const rows = this.parseCsv(csv);
    if (rows.length === 0) {
      el.createEl("div", { cls: "mg-grafeno-query__empty", text: "Consulta sem resultado." });
      return;
    }

    const table = el.createEl("table", { cls: "mg-grafeno-query__table" });
    const thead = table.createEl("thead");
    const headerRow = thead.createEl("tr");
    for (const heading of rows[0]) {
      headerRow.createEl("th", { text: heading });
    }

    const tbody = table.createEl("tbody");
    for (const row of rows.slice(1)) {
      const tr = tbody.createEl("tr");
      for (const value of row) {
        tr.createEl("td", { text: value });
      }
    }
  }

  parseCsv(csv) {
    const rows = [];
    let row = [];
    let field = "";
    let quoted = false;

    for (let i = 0; i < csv.length; i += 1) {
      const char = csv[i];
      const next = csv[i + 1];

      if (quoted) {
        if (char === '"' && next === '"') {
          field += '"';
          i += 1;
        } else if (char === '"') {
          quoted = false;
        } else {
          field += char;
        }
        continue;
      }

      if (char === '"') {
        quoted = true;
      } else if (char === ",") {
        row.push(field);
        field = "";
      } else if (char === "\n") {
        row.push(field);
        rows.push(row);
        row = [];
        field = "";
      } else if (char !== "\r") {
        field += char;
      }
    }

    row.push(field);
    rows.push(row);
    return rows.filter((currentRow) => currentRow.some((value) => value.length > 0));
  }
};
