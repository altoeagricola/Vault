---
title: Proxmox VE
type: Tool
cover: "[[Wiki/Tools/_covers/proxmox.png]]"
sources:
related:
  - "[[OPNsense]]"
  - "[[QEMU]]"
  - "[[Docker]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

Proxmox Virtual Environment (VE) is an open-source server virtualization platform that combines KVM/QEMU for virtual machines and LXC for lightweight containers under a unified web management interface. It is the hypervisor of choice for homelabs that need to run multiple isolated workloads on a single physical host.

## Use Cases

- **Hypervisor for homelab** — Run multiple VMs and containers on a single server with resource isolation
- **VM management** — Create, snapshot, clone, and migrate KVM virtual machines through the web UI or CLI
- **LXC containers** — Lightweight system containers for services that don't need full VM overhead
- **Backup and restore** — Scheduled backups to local or remote storage with Proxmox Backup Server integration
- **Clustering** — Join multiple Proxmox hosts into a cluster for HA and live migration

## Examples

### VM configuration snippet (`/etc/pve/qemu-server/100.conf`)

```conf
boot: order=scsi0;net0
cores: 4
memory: 8192
name: opnsense
net0: virtio=AA:BB:CC:DD:EE:FF,bridge=vmbr0
scsi0: local-lvm:vm-100-disk-0,size=32G
scsihw: virtio-scsi-single
```

### Create an LXC container via CLI

```bash
pct create 200 local:vztmpl/debian-12-standard_12.2-1_amd64.tar.zst \
  --hostname docker-host \
  --memory 4096 \
  --cores 2 \
  --rootfs local-lvm:16 \
  --net0 name=eth0,bridge=vmbr0,ip=10.0.1.60/24,gw=10.0.1.1 \
  --features nesting=1 \
  --start 1
```

### Add NFS storage

```bash
pvesm add nfs backups \
  --server 10.0.1.10 \
  --export /mnt/backups \
  --content backup,iso
```

## Links

- **Official site:** https://www.proxmox.com/proxmox-ve
- **Repository:** https://git.proxmox.com
- **Documentation:** https://pve.proxmox.com/wiki/Main_Page
