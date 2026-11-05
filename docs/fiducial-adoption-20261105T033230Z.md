# Fiducial adoption

Evidence class: contract-verified. Claude Code /context and Codex hook trust: not live-verified by this procedure.

Changed paths:

- `.agents/skills/adopt/SKILL.md`
- `.claude/fiducial-ownership.json`
- `.claude/skills/adopt/SKILL.md`
- `AGENTS.md`
- `CLAUDE.md`

## Inventory

```json
{
  ".agents/skills/adopt/SKILL.md": {
    "mode": 420,
    "sha256": "e6254d6138783a3157d5b972717e0695eafda0689ac69193ea077548c889ef7b"
  },
  ".agents/skills/build/SKILL.md": {
    "mode": 420,
    "sha256": "2f1558cdf74c3b1b3ff47fff2ec9d717a31175bba04700d1a0ec61fcd83c0ecc"
  },
  ".agents/skills/change-flow/SKILL.md": {
    "mode": 420,
    "sha256": "63d81daacf5653a61987c171f3541ac703e3d279606cea567028260d75c421bf"
  },
  ".agents/skills/decision-log/SKILL.md": {
    "mode": 420,
    "sha256": "68762cc13dc972c0c3767684692e087894fac2dde9814356c0ae8e1d649dad29"
  },
  ".agents/skills/gate/SKILL.md": {
    "mode": 420,
    "sha256": "fd9709776ac6f3aa8c07ce74c0c92c018a74e3cede31c134ba37007f62fbea22"
  },
  ".agents/skills/intake/SKILL.md": {
    "mode": 420,
    "sha256": "f61e3c64c87b6ed8f1919131f51d522db7129c06f417af31fe5ca2190ee09fc5"
  },
  ".agents/skills/outline/SKILL.md": {
    "mode": 420,
    "sha256": "3bdd968474327c7aa5d2cda7fac596fc934442fca03bcfe3a8b52c7a65356702"
  },
  ".agents/skills/project-status/SKILL.md": {
    "mode": 420,
    "sha256": "7447b9a2e504cbe10351a68ddac411be1fee51cc1a45f210a0d58fa7bdeecd0c"
  },
  ".agents/skills/release/SKILL.md": {
    "mode": 420,
    "sha256": "0adf1fac839e16c7a53e07101839c010676f96607b39f57a9d4acac6ff115c7c"
  },
  ".agents/skills/retro/SKILL.md": {
    "mode": 420,
    "sha256": "705f4f53ab3f386fdbd989757aecaf904be7d647ea07ce6598b716c95c0c84f5"
  },
  ".agents/skills/review-artifact/SKILL.md": {
    "mode": 420,
    "sha256": "3ea8f4ee63b9aead12791293c474c7aa74918ffce410919e71468916afeb059c"
  },
  ".agents/skills/spec-template/SKILL.md": {
    "mode": 420,
    "sha256": "cf53edd282d3e253b971e84fef83cad92811f9833d1b8f210d8f3ec9d3f9686c"
  },
  ".agents/skills/voice/SKILL.md": {
    "mode": 420,
    "sha256": "6c3838183382ffbd74c67d2ae824278aeed8ba24541cdd6ff50cbd674b63357d"
  },
  ".claude/agents/architect-agent.md": {
    "mode": 420,
    "sha256": "3aaa4b92bc195fcbca90eda0301ced27a543d7ca092784301c5b576256a6f504"
  },
  ".claude/agents/coder-agent.md": {
    "mode": 420,
    "sha256": "81d89984fd3f3e1e2011691f7ace2ca0ee6aa34f6b9607005038895c18760cb1"
  },
  ".claude/agents/context-quality-reviewer.md": {
    "mode": 420,
    "sha256": "17bbd49f96123b79e608d8c6c7920e33bda819fdea2751cd0e0515c486225d53"
  },
  ".claude/agents/release-manager-agent.md": {
    "mode": 420,
    "sha256": "0a93ab34bb77a023b74728cb416a67db3b38c4a0ed27ff9c59bf9a9209966439"
  },
  ".claude/agents/reviewer-agent.md": {
    "mode": 420,
    "sha256": "88053b66b87d934a0ece3cca4a376fbefdcaa0a9e5a8748d280b8ea558d8bd0f"
  },
  ".claude/agents/skeptic-risk-agent.md": {
    "mode": 420,
    "sha256": "503e97195023f7dcfd1c5db51122f17ca00142dff180036adeca111d5bcb05b2"
  },
  ".claude/agents/spec-reviewer-agent.md": {
    "mode": 420,
    "sha256": "06376f049061266d37b149c72e37af99917cd1ab3482c0eb3a6214812571ce43"
  },
  ".claude/agents/test-designer-agent.md": {
    "mode": 420,
    "sha256": "d3d606b3f4614fa59be0a4a8a531c82156ae193e6e80abd2df49e6c9136abc29"
  },
  ".claude/fiducial-ownership.json": {
    "mode": 420,
    "sha256": "fe954e9750339c84d251c5e8d8fe6ed38a2ea4b055fe66eab2d2804b2c2cfdcb"
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
    "sha256": "6ef24c3c09d2f749aef067b6ddba3d1d5ab3f3679e02c6af2b8daa9ba7fa9319"
  },
  ".claude/skills/build/SKILL.md": {
    "mode": 420,
    "sha256": "3d3a6b0d620f4483602880e92306e48624335e6b28a9f7486bb579fa709be500"
  },
  ".claude/skills/change-flow/SKILL.md": {
    "mode": 420,
    "sha256": "5228f02ebaa65fd80446888f4958f4892b8dfe7a8699273bc40874ed6713300e"
  },
  ".claude/skills/decision-log/SKILL.md": {
    "mode": 420,
    "sha256": "cffed38b4d1b4fdbb66dbcc21e8af0697bc1910bef8a1988473ea9258cb4836a"
  },
  ".claude/skills/gate/SKILL.md": {
    "mode": 420,
    "sha256": "82d0ea2f99e396217b13c63dc45eafcf0c83a64036af4f75bf0117fb45ec289d"
  },
  ".claude/skills/intake/SKILL.md": {
    "mode": 420,
    "sha256": "6ae2d32faccf7bc883a17132e5957200c55909ab2b2b6830d12314863f6ee9ba"
  },
  ".claude/skills/outline/SKILL.md": {
    "mode": 420,
    "sha256": "99757858c68e1a87247d266f3bf8323916b8b0be9df2429b03d9a4d46d518d4f"
  },
  ".claude/skills/project-status/SKILL.md": {
    "mode": 420,
    "sha256": "2002d01965bd727bab1863513502ac5082080d0ab7045acd76d0eda74aa1bda0"
  },
  ".claude/skills/release/SKILL.md": {
    "mode": 420,
    "sha256": "2ef1ad81893726965686b0f2f2c1f06219f92a94d2703eb3a0291ddba3a59ece"
  },
  ".claude/skills/retro/SKILL.md": {
    "mode": 420,
    "sha256": "99da638818aed09b534dc7f1c600dd8f1adea15e833ba2494904efc50fd7ddfb"
  },
  ".claude/skills/review-artifact/SKILL.md": {
    "mode": 420,
    "sha256": "5bdff8eb000e15b219d280e78076c76d6dcae510d1153fbef93f18eaa833d088"
  },
  ".claude/skills/spec-template/SKILL.md": {
    "mode": 420,
    "sha256": "3d53a66f5bf438876401d67a8a4543d2e89e67327a94aeefc06324fd59cdcc2e"
  },
  ".claude/skills/voice/SKILL.md": {
    "mode": 420,
    "sha256": "359cf529fbc03f8550bd60c81f3741230de6e37f50deebd560845c220d779473"
  },
  ".codex/agents/architect-agent.toml": {
    "mode": 420,
    "sha256": "f87f2d59555f24e3d3f3dbdd5c3597db989e4cfcc969461b52b7cd5178e684f8"
  },
  ".codex/agents/coder-agent.toml": {
    "mode": 420,
    "sha256": "85f7c1d349a897f6b868f02a6a637e5b33e58fa6126d47c6708d56e6d0cebd67"
  },
  ".codex/agents/context-quality-reviewer.toml": {
    "mode": 420,
    "sha256": "bd5bb7bebbe47b7f7f1a1b7f2218912ae2e824dbbc3a738bcaa57cde583fa55e"
  },
  ".codex/agents/release-manager-agent.toml": {
    "mode": 420,
    "sha256": "4a2a55af2dbd4a9bcaed30fed91633ed669227c0807fbf548357a57bbf008f81"
  },
  ".codex/agents/reviewer-agent.toml": {
    "mode": 420,
    "sha256": "0cdff4f96b2b5b3f7343c7550994f280628f14c55d6492d5bd9a94fde2293ba4"
  },
  ".codex/agents/skeptic-risk-agent.toml": {
    "mode": 420,
    "sha256": "f14d5546708313e218dbff43f3d0cabd33979e8a8534f6543080cf437f55f58f"
  },
  ".codex/agents/spec-reviewer-agent.toml": {
    "mode": 420,
    "sha256": "383a79ab61e7d448c86f6de7ca54836975c3f04ee9793d64c630158813a5142c"
  },
  ".codex/agents/test-designer-agent.toml": {
    "mode": 420,
    "sha256": "70fdedf4b69512bf0da4a25b1a1e8876b61947715aaa5a4c2bb3f97f2b02bcfb"
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
    "sha256": "5d7d0eca4c5e5fc3011718e7c38174e484eecd09ae74b4b73de5252ac2c0ddac"
  },
  "CLAUDE.md": {
    "mode": 420,
    "sha256": "5d7d0eca4c5e5fc3011718e7c38174e484eecd09ae74b4b73de5252ac2c0ddac"
  }
}
```

## Independent contradiction read

```json
{
  "plan_sha256": "d6600cc35af4efc93a0d85e365b33c5767853be420aa85044dca0a7f55426667",
  "reviewer": "pkg7_close_reviewer — same independent frontier reviewer; amendment-only semantic contradiction read, no human approval",
  "findings": []
}

```

## Human rulings

```json
{
  "authorization": "Dave explicitly approved the complete package 7 continuity amendment and same-reader review on 2026-11-04. This applies only its independently reviewed derived-context regeneration on the unmerged intake branch; human merge and release remain reserved. No new contradiction was found.",
  "gate": "routine",
  "go": true,
  "human": "Dave Pierce",
  "plan_sha256": "d6600cc35af4efc93a0d85e365b33c5767853be420aa85044dca0a7f55426667",
  "review_sha256": "924ef85d629e4b9da43a8e3b0692292be46b4d9b60a24b2316f3b14a25b8f36b",
  "rulings": {}
}
```

## Exact legacy edits

```json
[]
```


## Package 7 regeneration evidence

Observed, contract-verified: source 15da4ad0b8780b60600cbb522825f5f4bded8683 on the intake branch, with a clean source diff at prepare; target starts at that same commit and retains its previously adopted harness inventory. The source origin is the canonical Fiducial GitHub repository. Execution was local on the human's macOS machine with restricted network access; staging, installation, lint and regeneration did not call a production system.

The same independent frontier reader inspected the amendment, intake rubric and complete semantic candidate diff in reviews/pkg-7-close-amendment-read-20261105T033515Z.md. No new contradiction was found. Dave explicitly approved the complete continuity amendment; this installation prepares its derived context in the unmerged PR, and authorizes neither merge nor release.

Observed, contract-verified: after apply, all five write destinations equal the independently reviewed plan bytes and permission modes. A fresh prepare using a detached source at the same 15da4ad pin returns writes={} and conflicts=[]; no second apply is claimed. Existing settings, denies, executable hooks, agent files and unrelated skills remain unchanged. The ownership manifest matches the four replaced Markdown sections.

Observed, contract-verified: bin/tests/run over the amended source passed 303 tests in 94.126 seconds, with no failures or skips; the independent reader separately checked the four changed rules and both complete emissions. The subsequent installation changes only the five already-reviewed generated files, with exact byte/mode read-back. Full test output is /private/tmp/fiducial-pkg7-tests-amended.log; its digest is recorded in the amendment review.

Project setup and forge labels are unchanged from the package 6b report; this regeneration made no forge configuration or label mutation and does not claim a new live protection audit. Human merge and release remain required. The new installed roots contain 295 lines including ownership markers; the emitter's warning is governed by DEC-001640. Native harness enforcement, project trust and fresh loading of this amended context remain unverified (deferred); earlier Illuminait loading evidence covers only its previously observed revision.
