# Changelog

## [Unreleased]

### Added

- Rust 与 Python SDK 新增受控工作负载 API，支持创建、查询和删除工作负载。
- 工作负载支持具名 TCP/UDP 多端点，并可对全部公开端点启动抓包和获取 PCAP 数据。
- 新增工作负载 v1 JSON Schema 与跨语言黄金 fixture。
- 新增 workload HTTP 路径、Bearer 认证、响应解析及严格 SemVer 校验测试。

### Changed

- Runtime v1 描述新增必填的 `platformVersion`，并在 Rust、Python 与 JSON Schema 中统一执行严格 SemVer 校验。
- Rust 发布校验现在会解包生成的 `.crate` 并运行完整测试，确保发布包可独立验证。
- Rust crate 内置测试 fixture，并在源码仓库测试中校验其与共享契约 fixture 保持同步。

## [0.1.0-alpha.1] - 2026-08-04

### Added

- 提供 Rust 与 Python 套件 Runtime SDK。
- 支持 UDS、mTLS HTTPS、实例能力校验和语义操作事件上报。
