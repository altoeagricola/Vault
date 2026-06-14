---
title: QEMU
type: Tool
cover: "[[Wiki/Tools/_covers/qemu.png]]"
sources:
  - InfraKeeper
related:
  - "[[Proxmox VE]]"
  - "[[UTM]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

QEMU (Quick Emulator) is an open-source machine emulator and virtualizer that can perform full system emulation of dozens of CPU architectures and hardware-accelerated virtualization via KVM (Linux) or Hypervisor.framework (macOS). It is the engine behind Proxmox, UTM, and many cloud platforms.

## Use Cases

- **VM backend for Proxmox and UTM** — Powers the virtualization layer in popular platforms
- **Hardware emulation** — Emulate ARM on x86, RISC-V on ARM, or any supported architecture combination
- **Disk image management** — Create, convert, and resize disk images in multiple formats (qcow2, raw, vmdk)
- **Device passthrough** — Pass physical PCI/USB devices directly to virtual machines
- **Live migration** — Move running VMs between hosts with zero downtime

## Examples

### Launch a VM

```bash
# Boot a Linux VM with KVM acceleration
qemu-system-x86_64 \
  -enable-kvm \
  -m 4G \
  -smp 4 \
  -drive file=disk.qcow2,format=qcow2 \
  -cdrom ubuntu.iso \
  -boot d

# ARM64 VM on macOS with Hypervisor.framework
qemu-system-aarch64 \
  -machine virt,accel=hvf \
  -cpu host \
  -m 2G \
  -drive file=arm-disk.qcow2,format=qcow2
```

### Disk image management

```bash
# Create a 20GB qcow2 disk
qemu-img create -f qcow2 disk.qcow2 20G

# Convert vmdk to qcow2
qemu-img convert -f vmdk -O qcow2 disk.vmdk disk.qcow2

# Resize a disk image
qemu-img resize disk.qcow2 +10G

# Show image info
qemu-img info disk.qcow2
```

### PCI/USB passthrough

```bash
# USB device passthrough
qemu-system-x86_64 \
  -enable-kvm \
  -m 4G \
  -usb \
  -device usb-host,vendorid=0x1234,productid=0x5678 \
  -drive file=disk.qcow2,format=qcow2
```

## Links

- **Official site:** https://www.qemu.org
- **Repository:** https://github.com/qemu/qemu
- **Documentation:** https://www.qemu.org/documentation/
