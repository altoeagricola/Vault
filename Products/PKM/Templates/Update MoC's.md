<%*
// ── Auto Catalog · Startup Template ───────────────────────────
// Place in your templates folder and set as Templater's
// "Startup Template" in Settings > Templater > Startup Template.
//
// Any note tagged "moc" (case-insensitive) that contains the
// Begin/End Catalog markers becomes an auto-updating catalog.
// The scan root is the folder where the catalog note lives.
//
// Folder notes: if a file has the same basename as its parent
// folder, or is named SKILL.md, the folder label becomes a
// wikilink to that file and the file is not listed separately.

const BEGIN_MARKER = "%% Begin Catalog %%";
const END_MARKER   = "%% End Catalog %%";
const MOC_TAG      = "moc";
const LISTENER_KEY = "_autoCatalogListeners";

// Basenames (without extension) that are treated as folder notes
const FOLDER_NOTE_NAMES = ["SKILL"];

// ── Cleanup previous listeners ─────────────────────────────────
if (window[LISTENER_KEY]) {
    for (const ref of window[LISTENER_KEY]) {
        app.vault.offref(ref);
    }
}
window[LISTENER_KEY] = [];

// ── Check if a file has the MoC tag ────────────────────────────
function hasMocTag(file) {
    const cache = app.metadataCache.getFileCache(file);
    const fm = cache?.frontmatter;
    if (!fm) return false;

    let tags = fm.tags ?? fm.tag ?? [];
    if (typeof tags === "string") tags = [tags];
    if (!Array.isArray(tags)) return false;

    return tags.some(t =>
        String(t).replace(/^#/, "").toLowerCase() === MOC_TAG
    );
}

// ── Check if a file is a folder note ───────────────────────────
function isFolderNote(entry) {
    return entry.basename === entry.parentName
        || FOLDER_NOTE_NAMES.includes(entry.basename);
}

// ── Find all catalog notes ─────────────────────────────────────
function getCatalogNotes() {
    return app.vault.getMarkdownFiles().filter(f => hasMocTag(f));
}

// ── Resolve display name from frontmatter ──────────────────────
function getDisplayName(file) {
    const fc = app.metadataCache.getFileCache(file);
    const ffm = fc?.frontmatter;
    return ffm?.name ?? ffm?.title ?? file.basename;
}

// ── Build a folder tree from a flat list of files ──────────────
function buildTree(files, root) {
    const tree = { files: [], subfolders: {}, folderNote: null };

    for (const entry of files) {
        const relative = entry.path.substring(root.length + 1);
        const parts = relative.split("/");
        parts.pop();

        let node = tree;
        for (const folder of parts) {
            if (!node.subfolders[folder]) {
                node.subfolders[folder] = { files: [], subfolders: {}, folderNote: null };
            }
            node = node.subfolders[folder];
        }

        if (isFolderNote(entry)) {
            node.folderNote = entry;
        } else {
            node.files.push(entry);
        }
    }

    return tree;
}

// ── Render tree as nested markdown list ─────────────────────────
function renderTree(node, indent) {
    const lines = [];
    const pad = "    ".repeat(indent);

    // Files first, sorted by display name
    const sortedFiles = node.files.sort((a, b) =>
        a.displayName.localeCompare(b.displayName)
    );
    for (const f of sortedFiles) {
        lines.push(`${pad}- [[${f.path}|${f.displayName}]]`);
    }

    // Then subfolders, sorted by folder name
    const sortedFolders = Object.entries(node.subfolders).sort((a, b) =>
        a[0].localeCompare(b[0])
    );
    for (const [folderName, subNode] of sortedFolders) {
        if (subNode.folderNote) {
            const fn = subNode.folderNote;
            lines.push(`${pad}- [[${fn.path}|${fn.displayName}]]`);
        } else {
            lines.push(`${pad}- **${folderName}**`);
        }
        lines.push(...renderTree(subNode, indent + 1));
    }

    return lines;
}

// ── Update a single catalog note ───────────────────────────────
async function updateCatalog(catalogFile) {
    const root = catalogFile.parent?.path;
    if (!root) return;

    const mdFiles = app.vault.getMarkdownFiles().filter(f => {
        if (f.path === catalogFile.path) return false;
        return f.path.startsWith(root + "/");
    });

    const entries = mdFiles.map(file => ({
        displayName: getDisplayName(file),
        path: file.path,
        basename: file.basename,
        parentName: file.parent?.name ?? "",
    }));

    const tree = buildTree(entries, root);
    const lines = ["", ...renderTree(tree, 0), ""];

    const content = await app.vault.read(catalogFile);
    const beginIdx = content.indexOf(BEGIN_MARKER);
    const endIdx = content.indexOf(END_MARKER);
    if (beginIdx === -1 || endIdx === -1) return;

    const before = content.substring(0, beginIdx + BEGIN_MARKER.length);
    const after = content.substring(endIdx);
    const newContent = before + "\n" + lines.join("\n") + "\n" + after;

    if (newContent !== content) {
        await app.vault.modify(catalogFile, newContent);
    }
}

// ── Update all catalogs ────────────────────────────────────────
async function updateAllCatalogs() {
    const catalogs = getCatalogNotes();
    for (const cat of catalogs) {
        await updateCatalog(cat);
    }
}

// ── Update only catalogs affected by a path change ─────────────
async function updateAffectedCatalogs(changedPath) {
    const catalogs = getCatalogNotes();
    for (const cat of catalogs) {
        const root = cat.parent?.path;
        if (root && changedPath.startsWith(root + "/")) {
            await updateCatalog(cat);
        }
    }
}

// ── Debounce ───────────────────────────────────────────────────
let debounceTimer = null;
function debouncedUpdate(path) {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => updateAffectedCatalogs(path), 1000);
}

// ── Register vault event listeners ─────────────────────────────
const onCreate = app.vault.on("create", (file) => {
    if (file.path?.endsWith(".md")) debouncedUpdate(file.path);
});
const onDelete = app.vault.on("delete", (file) => {
    if (file.path?.endsWith(".md")) debouncedUpdate(file.path);
});
const onRename = app.vault.on("rename", (file, oldPath) => {
    if (file.path?.endsWith(".md")) {
        debouncedUpdate(file.path);
        debouncedUpdate(oldPath);
    }
});

window[LISTENER_KEY] = [onCreate, onDelete, onRename];

// ── Initial update ─────────────────────────────────────────────
setTimeout(() => updateAllCatalogs(), 2000);
_%>