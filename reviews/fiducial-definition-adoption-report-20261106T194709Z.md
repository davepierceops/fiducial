# Fiducial adoption

Evidence class: contract-verified. Claude Code /context and Codex hook trust: not live-verified by this procedure.

Changed paths:

- `.agents/skills/command-blocks/SKILL.md`
- `.agents/skills/spec-template/SKILL.md`
- `.claude/fiducial-ownership.json`
- `.claude/skills/command-blocks/SKILL.md`
- `.claude/skills/spec-template/SKILL.md`
- `AGENTS.md`
- `CLAUDE.md`

## Inventory

```json
{
  ".agents/skills/adopt/SKILL.md": {
    "mode": 420,
    "sha256": "f7680a305c7a5b5d83f0d15c2e4221b7df0bd1a673e46cf55c9f1fc1aa268282"
  },
  ".agents/skills/build/SKILL.md": {
    "mode": 420,
    "sha256": "b11386c84eda7fa77081121367d4375e75fe4509f865b45174672f5a839c8a60"
  },
  ".agents/skills/change-flow/SKILL.md": {
    "mode": 420,
    "sha256": "6d8ad35b8dcc5dca23187d1dd93772060a92855e50a905f0dcb11e3b9d3a4aae"
  },
  ".agents/skills/command-blocks/SKILL.md": {
    "mode": 420,
    "sha256": "abc67b4929066f92eb549526d885f984266cc4dfbffc3ccaa6ff9e51dd9ee081"
  },
  ".agents/skills/decision-log/SKILL.md": {
    "mode": 420,
    "sha256": "acec63426cefec4291fcae9da7c824aa7c6ffeea06ca166acc858197b783978a"
  },
  ".agents/skills/gate/SKILL.md": {
    "mode": 420,
    "sha256": "979103f52eb6e3c78cf47bfc54e6a1135571d1b3b5668763eb1f41dd4d5134d6"
  },
  ".agents/skills/intake/SKILL.md": {
    "mode": 420,
    "sha256": "f9f8c190e3c38a337f7036463a45339153082e941ae20bd8fc353fcd68938fe3"
  },
  ".agents/skills/outline/SKILL.md": {
    "mode": 420,
    "sha256": "3bdd968474327c7aa5d2cda7fac596fc934442fca03bcfe3a8b52c7a65356702"
  },
  ".agents/skills/project-status/SKILL.md": {
    "mode": 420,
    "sha256": "4c40334ae71fddd067f9000bf2abab7da1c5cd1f0b309f47e8a24ea1dd8b0870"
  },
  ".agents/skills/release/SKILL.md": {
    "mode": 420,
    "sha256": "35b26c52e0984b9b58107e92e7a022d328158631d16f97e7da99a3b74fe32561"
  },
  ".agents/skills/retro/SKILL.md": {
    "mode": 420,
    "sha256": "99fb3e421ca6cb90bc4260950bdfdcfa4719a5fc88437b4bcfa7f925e8ebfbf4"
  },
  ".agents/skills/review-artifact/SKILL.md": {
    "mode": 420,
    "sha256": "a1acb54a2b896669bfeac4ff5b19ad3647a0f35ae343194c02071b3ce0694a01"
  },
  ".agents/skills/spec-template/SKILL.md": {
    "mode": 420,
    "sha256": "f1e6af0f318d9609efcf047440a2b9f5ab60b2a5189f837f0f3d8c85cc2402b5"
  },
  ".agents/skills/verification-checklists/SKILL.md": {
    "mode": 420,
    "sha256": "f9156f44a9b8d689de1b4f2c435096348f8e9a8e51d0655004c04c40be1dae03"
  },
  ".agents/skills/voice/SKILL.md": {
    "mode": 420,
    "sha256": "4838263bcf65bd56841ecebe380e87f3a3c292e6985f155e4a71ecf774026ce4"
  },
  ".claude/agents/architect-agent.md": {
    "mode": 420,
    "sha256": "5a5a6186c230596be6bbab8397e8908f570e2df964e9800487262eb21ebdee2b"
  },
  ".claude/agents/coder-agent.md": {
    "mode": 420,
    "sha256": "8fe83e6922e96c31f13e983c2f0769a73b6f9364aaa277eae14deee01344d2af"
  },
  ".claude/agents/context-quality-reviewer.md": {
    "mode": 420,
    "sha256": "ac2a80a85aab2199e1e2ca21edf3428bea5a696116f2ac2ba54200650e3f3bfa"
  },
  ".claude/agents/release-manager-agent.md": {
    "mode": 420,
    "sha256": "04b35d30bc30568581f52d73518146c26ce9f55d2dcae14e48805ecf165f2a6d"
  },
  ".claude/agents/reviewer-agent.md": {
    "mode": 420,
    "sha256": "baae6fc0885a797f321f4c25326230967da792e097e0f41c04eaca00c628728a"
  },
  ".claude/agents/skeptic-risk-agent.md": {
    "mode": 420,
    "sha256": "e0b48143576e44d3d5ebb87e076b6c7e95f203ebf6ead6c8bf78cab4fe834ccb"
  },
  ".claude/agents/spec-reviewer-agent.md": {
    "mode": 420,
    "sha256": "f431484ebc7efe126e118f26d89feee59b31b0f78e4226ec0be90ae7535b220d"
  },
  ".claude/agents/test-designer-agent.md": {
    "mode": 420,
    "sha256": "3c11ba91dd9d2cd67a1d93864c7979b7dcdf280934974194f909f86ff7e66738"
  },
  ".claude/fiducial-ownership.json": {
    "mode": 420,
    "sha256": "14397a8030baab697117fc29be8565e4b6f8cbd2105bd930c67d5853e68e7c06"
  },
  ".claude/hooks/_hooklib.py": {
    "mode": 493,
    "sha256": "a53f54c7fe50154d914ee68c48ee1a38e1801fd99780d27040c8df91f5b4e561"
  },
  ".claude/hooks/decision-log-append-only": {
    "mode": 493,
    "sha256": "4a85c5c6245f59abc7dd93dd3a56be3dc8f883bacb4a4ff5c8b8f17cc87f24e5"
  },
  ".claude/hooks/intake-branch-guard": {
    "mode": 493,
    "sha256": "46bf241151ae96bbe81b9a6b7246f6227eca7c0c9f4e277e262773c2a76caa11"
  },
  ".claude/hooks/lane-guard": {
    "mode": 493,
    "sha256": "64da9ab62c235ba2ae7362423cc978cc4fb9be4e729b8de8a978a93ef8c8d733"
  },
  ".claude/hooks/push-readback": {
    "mode": 493,
    "sha256": "0fbcc78a8f03d161a21214167a14dab710f29d576994ce42c69b7ceb2aa846e5"
  },
  ".claude/hooks/review-artifact-immutable": {
    "mode": 493,
    "sha256": "1300f9bda0e410484a62c08ec5f882715f9851e5c9d3f3673b5ea1070f21b0b4"
  },
  ".claude/hooks/store-lint": {
    "mode": 493,
    "sha256": "c7477bf16f9c6e8e92d53700298f0c0cbc7b32d26450630d1ce70b8705f4e47b"
  },
  ".claude/settings.json": {
    "mode": 420,
    "sha256": "a7a60fbb34d1de14eb518420adbc1d0d1f3d411cad5a5d6954e7072afc0c11b0"
  },
  ".claude/skills/adopt/SKILL.md": {
    "mode": 420,
    "sha256": "e552540ef81f95c4e8b5e8955d394800717afdde1b9213ca301e461bdc9fae35"
  },
  ".claude/skills/build/SKILL.md": {
    "mode": 420,
    "sha256": "c73b83eb02bca5c2633333bf9ab18261889759b3a4db340f0e66c2fa08ed0da1"
  },
  ".claude/skills/change-flow/SKILL.md": {
    "mode": 420,
    "sha256": "ed1d819d32376d5ef839ba3c3406f231c66ecc78895a908f2d01719a81db0c16"
  },
  ".claude/skills/command-blocks/SKILL.md": {
    "mode": 420,
    "sha256": "52684bd10c4fbaa14fca576c84e38e49747988e7736aa1bf14daa095bcfcd431"
  },
  ".claude/skills/decision-log/SKILL.md": {
    "mode": 420,
    "sha256": "b196b3b3dd7588920a17383d546ae9d4927087396c108f399c7362513c1ca3fa"
  },
  ".claude/skills/gate/SKILL.md": {
    "mode": 420,
    "sha256": "628e93b9a5291fccf445ef405b0fa5f913d2f33bba7990d3bab92aeea227f545"
  },
  ".claude/skills/intake/SKILL.md": {
    "mode": 420,
    "sha256": "25af9f3962430af01c24b2a383940feeefc409218286a999d61a5b100804e303"
  },
  ".claude/skills/outline/SKILL.md": {
    "mode": 420,
    "sha256": "99757858c68e1a87247d266f3bf8323916b8b0be9df2429b03d9a4d46d518d4f"
  },
  ".claude/skills/project-status/SKILL.md": {
    "mode": 420,
    "sha256": "6e8ce526b52d8961918ee569d18fb3b8910c6940a5f1f04438277299f64c5e32"
  },
  ".claude/skills/release/SKILL.md": {
    "mode": 420,
    "sha256": "6ac3484411d8e128f5dd033077026228285900560c2a82ff30ce0596bf1bf274"
  },
  ".claude/skills/retro/SKILL.md": {
    "mode": 420,
    "sha256": "13a58071a9e7a6b02053a563420b9cadfc2e8ed9185e45e69d67a1f3466bd4e6"
  },
  ".claude/skills/review-artifact/SKILL.md": {
    "mode": 420,
    "sha256": "7f50956e325c3c34c80e0ca997da21e49579aea7fcdfa2244be9ba6f645d54ac"
  },
  ".claude/skills/spec-template/SKILL.md": {
    "mode": 420,
    "sha256": "4590bd9eea4fa520ff68f8d92d873fdf1e3a5c4b42051e2762956cf33a73e737"
  },
  ".claude/skills/verification-checklists/SKILL.md": {
    "mode": 420,
    "sha256": "17e8273215a698cb9c7284381123a45bb56726209ebce75d90c48b2a3b4c37e2"
  },
  ".claude/skills/voice/SKILL.md": {
    "mode": 420,
    "sha256": "9e7178b8ae0b68afb1b5315aebf4fe739a99e1555fc2a37f9b0ec45a623f0ec2"
  },
  ".codex/agents/architect-agent.toml": {
    "mode": 420,
    "sha256": "400dd85f19836c94b758ad3b9b4daec6f193bc476c1ea2ac137d778b55c5d39d"
  },
  ".codex/agents/coder-agent.toml": {
    "mode": 420,
    "sha256": "11a9aa8d0756b46dc0b4d8774017be2ecd61f112c78e3936143442bdead7d7a1"
  },
  ".codex/agents/context-quality-reviewer.toml": {
    "mode": 420,
    "sha256": "221cf8d01f55d5483bf8f61f5b3d3ff270e0985ddba766efec4c4d9ad188395b"
  },
  ".codex/agents/release-manager-agent.toml": {
    "mode": 420,
    "sha256": "9c4b18d488273b08f76db25e80af6b68fc6f7536a8fc292872ea8e5ffd8d1c76"
  },
  ".codex/agents/reviewer-agent.toml": {
    "mode": 420,
    "sha256": "93100efb9ffcfde6d7d95e50642c1fb5f4f54f0e9931abf0cc375b7162fa37db"
  },
  ".codex/agents/skeptic-risk-agent.toml": {
    "mode": 420,
    "sha256": "7cc1e92c37b7927a8eda0b1ff1f6dd64c7a8ad7b8a81ff2891af59eac944554a"
  },
  ".codex/agents/spec-reviewer-agent.toml": {
    "mode": 420,
    "sha256": "c421abbefbd755a7efdd46fc7b038d5aca34beb191664972d0f6199d18aac354"
  },
  ".codex/agents/test-designer-agent.toml": {
    "mode": 420,
    "sha256": "434d116b1dcc721facf6a24211ed92c464f4a35ad97426940573664ec9c445bd"
  },
  ".codex/hooks.json": {
    "mode": 420,
    "sha256": "cd592f0347157960b7aafc2f914e72305c255de754d56efd2836393230d9f525"
  },
  ".codex/hooks/_hooklib.py": {
    "mode": 493,
    "sha256": "a53f54c7fe50154d914ee68c48ee1a38e1801fd99780d27040c8df91f5b4e561"
  },
  ".codex/hooks/codex-hook": {
    "mode": 493,
    "sha256": "854bc61e268a857adc8ba2096cc976ab0cb711ea15c1b122c13093c5b9612bec"
  },
  ".codex/hooks/decision-log-append-only": {
    "mode": 493,
    "sha256": "4a85c5c6245f59abc7dd93dd3a56be3dc8f883bacb4a4ff5c8b8f17cc87f24e5"
  },
  ".codex/hooks/intake-branch-guard": {
    "mode": 493,
    "sha256": "46bf241151ae96bbe81b9a6b7246f6227eca7c0c9f4e277e262773c2a76caa11"
  },
  ".codex/hooks/lane-guard": {
    "mode": 493,
    "sha256": "64da9ab62c235ba2ae7362423cc978cc4fb9be4e729b8de8a978a93ef8c8d733"
  },
  ".codex/hooks/push-readback": {
    "mode": 493,
    "sha256": "0fbcc78a8f03d161a21214167a14dab710f29d576994ce42c69b7ceb2aa846e5"
  },
  ".codex/hooks/review-artifact-immutable": {
    "mode": 493,
    "sha256": "1300f9bda0e410484a62c08ec5f882715f9851e5c9d3f3673b5ea1070f21b0b4"
  },
  ".codex/hooks/store-lint": {
    "mode": 493,
    "sha256": "c7477bf16f9c6e8e92d53700298f0c0cbc7b32d26450630d1ce70b8705f4e47b"
  },
  "AGENTS.md": {
    "mode": 420,
    "sha256": "24f5fbab20185b85fdbfcb1a58cb9812b07a53c55c3d88f6a450ef3df7f82188"
  },
  "CLAUDE.md": {
    "mode": 420,
    "sha256": "24f5fbab20185b85fdbfcb1a58cb9812b07a53c55c3d88f6a450ef3df7f82188"
  }
}
```

## Independent contradiction read

```json
{
  "plan_sha256": "3e657857a7d69029e6ee942e1af4627eff44644138231607d1ce216de64b75cc",
  "reviewer": "Independent Context Quality Reviewer / frontier process and adoption reader (definition_frontier_review); not an implementation author",
  "findings": []
}

```

## Human rulings

```json
{
  "authorization": "2026-11-06: Dave requested finalization, accepted leaving R0064 unchanged pending #425, then answered “go”. Exact per-row approvals are recorded in docs/plans/claude-definition-pruning-rulings-20261106T181925Z.md and DEC-001700.",
  "gate": "routine",
  "go": true,
  "human": "Dave",
  "plan_sha256": "3e657857a7d69029e6ee942e1af4627eff44644138231607d1ce216de64b75cc",
  "review_sha256": "8fb621df9dc19480768c5c66423a669d78e8f929d21bf19b0fdf2624c9864a0e",
  "rulings": {}
}
```

## Exact legacy edits

```json
[]
```

## Repository-specific evidence

- Source: davepierceops/fiducial at 6b473f90c9e7446de1f96207e25a56516378ee0f. Target at initial preparation: the same SHA; at application: 2e1dd71d3e5f4c2f124c41b51f3ebb61b7aee3ff (test-only commit). The uncommitted source difference during preparation was confined to the two test files subsequently committed at 2e1dd71; no emitter input differed from the source pin.
- Target: /private/tmp/fiducial-definition-pruning, intake/claude-definition-pruning. Local Python generation and file application; network access limited to Git/GitHub reads and authorized PR landing. No deployed service or other repository is adopted.
- Independent read: reviews/claude-definition-pruning-read-20261106T195037Z.md, ready in quality, skepticism and continuity; no contradictions. The reviewer checked all 66 inventory files, 65 generated files and seven candidate writes.
- Applied seven planned writes, then read back exact bytes and file modes for all seven. Native agent files, hook implementations, settings and existing local denies remain unchanged.
- Same-pin repeat prepare, using a detached checkout at 6b473f9, reports zero conflicts and zero writes. The independently reviewed repeat apply returned an empty write list; all existing adoption-report hashes were unchanged and no new report was created.
- Project-setup readback: default-branch protection disallows force push and deletion, applies to administrators and contains PR review configuration; runner deny mechanisms are unchanged and locally contract-tested. Live runner hook firing remains unverified.
- Existing human-gate, blocking, deferred, accepted-risk and not-material labels were read back; no labels were changed.
- Gate: routine context reconciliation under the recorded human finalization instruction “go,” per-row rulings and DEC-001700. R0064 remains unchanged and tracker portability is deferred to issue #425. No new unresolved human ruling was found in the independent read.
- Native loading, skill invocation/adherence and live enforcement are not established by source/output tests or byte readback. No production/browser/SLO checks apply to this context-only change.
