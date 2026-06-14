---
title: UTM
type: Tool
cover: "[[Wiki/Tools/_covers/utm.png]]"
sources:
  - InfraKeeper
related:
  - "[[Proxmox VE]]"
  - "[[Home Assistant]]"
  - "[[QEMU]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

UTM is a macOS-native virtualization application built on top of QEMU that provides a polished GUI for running virtual machines on Apple Silicon and Intel Macs. It supports both hardware-accelerated virtualization (Apple Virtualization framework) and full system emulation for running x86 operating systems on ARM hardware.

## Use Cases

- **Run Linux/Windows VMs on Mac** — Full desktop or server VMs with native or near-native performance on Apple Silicon
- **ARM and x86 emulation** — Run x86_64 operating systems on ARM Macs via QEMU translation
- **Headless server VMs** — Run background VMs for development servers, databases, or Kubernetes nodes
- **Device passthrough** — USB device passthrough and serial port emulation for hardware development
- **Snapshot management** — Take and restore VM snapshots for safe experimentation

## Examples

### Creating a VM

1. Download a Linux ISO (e.g., Ubuntu Server ARM64)
2. In UTM: File > New > Virtualize (for native ARM) or Emulate (for x86)
3. Select the ISO, configure RAM and disk size
4. Boot and install the OS

### QEMU backend options

UTM exposes QEMU settings for advanced configuration:
- **CPU:** Choose CPU model, core count, and features
- **Network:** Shared network (NAT), bridged, or host-only modes
- **Display:** VirtIO GPU, SPICE, or headless (serial console only)
- **Drives:** VirtIO, NVMe, or IDE disk backends

### Network bridging for homelab

```
Settings > Network > Network Mode: Bridged
Bridge Interface: en0
```

This gives the VM a real IP on your LAN — useful for running services like [[Home Assistant]] or [[Proxmox VE]] test environments.

## Links

- **Official site:** https://mac.getutm.app
- **Repository:** https://github.com/utmapp/UTM
- **Documentation:** https://docs.getutm.app
