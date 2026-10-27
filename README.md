# NieR iOS Native

Experimental iOS/iPadOS host changes for **NieR:Automata**, built on
[nxnative](https://github.com/seedds/nxnative). This repository consolidates our
Chinese launcher, controller integration, lifecycle/watchdog work, Metal command
reuse, present-completion backport, and bounded geometry-scratch experiment.

**This is source code for an experimental port, not a finished game download.**
You need your own game data and a compatible Apple build/signing environment.
No game executable, extracted shader, texture, ROM, key, save, or IPA is included.

## Current evidence and limitations

- A user reported a 30-minute session without a crash on the geometry-pool build.
- Crowded combat and large outdoor scenes can remain around 15 fps. Empty indoor
  scenes are smoother. Sustained 60 fps is **not** established.
- The 9S model can become purple in specific scenes. Its cause is unresolved.
- The single geometry pool waits for GPU completion on wrap; the retained log
  records many such drains. This is a suspected performance cost, not an isolated
  causal measurement. The pool is experimental and opt-in.
- Internal native resolution, full-screen projection/HUD, gameplay background
  recovery, and broad Bluetooth-controller compatibility are not accepted yet.
- CPU tests and macOS compilation do not validate iPad GPU correctness.

## Source layout and reproduction

`upstream.json` pins the exact source revision for `current-experimental.patch`.
The patch contains host source only and applies to that revision, not arbitrary
latest main. `prepare.py` checks out and verifies the pin, then checks and applies
the patch. It does not download games, sign, install, or launch anything.

```sh
python3 prepare.py /path/to/new/nier-host
```

Then follow the prepared checkout's `README.md` and `docs/development.md` to build
using your own files. Windows can prepare source; an Apple SDK/toolchain is still
required for the final iOS build. Do not upload game inputs to public Actions.

## Upstream updates

The launcher should follow nxnative's current single-screen, profile-driven
settings design and validated persistence model rather than accumulating custom
per-game controls. Chinese localization must preserve file-override locks and
only store settings that differ from the tested defaults.

Reviewed latest nxnative: `cdc6cef6b0250fcb54a061e4c55d56382b5d18ad`.
Relevant work includes unaligned vertex streams (`40e6baede556acd454169ac75b33d1686063f528`),
CPU-written texture lifetime tracking (`d6e6c575ef719c1b96de812dd7bbf700ccf39a94`),
and pipeline-archive compaction (`cdc6cef6b0250fcb54a061e4c55d56382b5d18ad`).
These are review targets, **not claimed fixes for the purple model**. Shader-chain
changes require rebuilding matching libraries; never mix libraries across chains.

See [REFERENCES.md](REFERENCES.md) for provenance and comparison.

## Contributing

Small, evidence-backed patches are welcome. State the source pin, device/OS,
scene, frame-time distribution, memory, and whether the issue reproduces before
and after. Redact personal identifiers from logs. Never submit game content,
keys, signing credentials, save files, or guest-memory captures. Preserve GPU
completion ownership; do not hide defects by skipping draws or recoloring output.

## 中文说明

这是《尼尔：机械纪元》原生 iOS/iPadOS 运行宿主的实验性源码整合项目。
整合了中文启动器、蓝牙手柄、后台恢复、命令缓冲复用和几何缓冲池的相关改动。
目前仍存在大场景严重掉帧、特定场景 9S 模型紫色等问题，尚未达到稳定 60 帧、
各设备原生内部分辨率和完整屏幕比例适配的目标。半小时未闪退是用户的一次测试
反馈，不代表全流程稳定。欢迎提交可复现的修复；仓库不提供游戏本体、密钥或 IPA。

## License

MIT for this host-source integration; original notices are retained in LICENSE.
Upstream dependencies keep their own licenses. This project is unofficial and
is not affiliated with the game's creators or platform vendors.

