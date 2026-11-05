# Fiducial adoption

Evidence class: contract-verified. Claude Code /context and Codex hook trust: not live-verified by this procedure.

Changed paths:

- `.claude/fiducial-ownership.json`
- `AGENTS.md`
- `CLAUDE.md`

## Inventory

```json
{
  ".agents/skills/adopt/SKILL.md": {
    "mode": 420,
    "sha256": "99b334a67c7d09ebf42f154dde7a2553216ddb862f33d45eb001967baf527ddb"
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
    "sha256": "b8ae01b5f53972c1013b62d9e1918813a49634217562c16c913efb00a4ae0017"
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
  ".claude/settings.local.json": {
    "mode": 420,
    "sha256": "73fa9245ade5be546d7784d90e63cf5518c91e259df88c429e955d51a19afb46"
  },
  ".claude/skills/adopt/SKILL.md": {
    "mode": 420,
    "sha256": "cda49201a786552d8b95b3dfcb24d62994cd3049af34817000db504d619e920d"
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
    "sha256": "847997f9381e7382b5e30dcbf6b2b2f32ce5ca0d5662ce3a43db233082613bcf"
  },
  "CLAUDE.md": {
    "mode": 420,
    "sha256": "847997f9381e7382b5e30dcbf6b2b2f32ce5ca0d5662ce3a43db233082613bcf"
  }
}
```

## Independent contradiction read

```json
{
  "plan_sha256": "31ecc88cfed5f12264c10a9694368020a64209bd4f3aa4b921f0f87ba4f37907",
  "reviewer": "independent adoption_review agent; Reviewer and Skeptic/Risk passes; solid general-purpose model tier",
  "findings": []
}

```

## Human rulings

```json
{
  "authorization": "User explicitly instructed \"adopt fiducial\" in this chat. Scope: routine self-adoption, now independently reviewed with no contradictions; exact candidate changes provenance comments and matching ownership hashes only. This records existing task authorization, not a new post-review response or merge/release approval.",
  "gate": "routine",
  "go": true,
  "human": "Dave Pierce",
  "plan_sha256": "31ecc88cfed5f12264c10a9694368020a64209bd4f3aa4b921f0f87ba4f37907",
  "review_sha256": "8af45ef88cdc5487522930e2e45a39de75a33e6b22f834d2c32f3c6b7ee50f30",
  "rulings": {}
}
```

## Exact legacy edits

```json
[]
```

## Execution and release readiness

Observed, contract-verified: source is the clean tagged checkout v2026.11.04 at 0ca563ee53c309840be4ab94dda74f9b075149ba; target baseline is 9c6fd4e6ba8df62f6b62c601d50910f0bfe0b88f. Source dirty diff is empty. The only target dirt before work was unrelated untracked retros/retro-20260917T041413Z.md, preserved. This run used local macOS/Python 3.15.2 with restricted egress; authenticated GitHub reads checked forge configuration and labels. No production system was touched.

Intent and acceptance: reconcile Fiducial's own installed context with the published source while preserving project-owned content. The independent review is reviews/fiducial-adoption-read-20261105T184649Z.md: quality, skepticism and continuity ready, no candidate contradictions. The three installed files match the reviewed plan bytes and modes. Only AGENTS.md and CLAUDE.md provenance comments and their ownership hashes change; user-visible behavior is unchanged. The prior comments named the pre-release amendment commit 15da4ad.

Test evidence: the extracted helper prepared and applied the actual target. A fresh prepare against the installed target returned writes={} and conflicts=[]. A disposable stand-in reproduced the identical inventory and writes, applied once, then returned an empty repeat plan and [] on repeat apply; every file hash, including its first adoption report, remained unchanged. Stand-in review/approval JSON was explicitly synthetic test data and supplied no real installation authority. The broad 303-test suite was not rerun for this provenance-only update; targeted generation, byte/mode verification and repeat checks cover its changed behavior. No code or instruction behavior changed.

Project setup: fresh authenticated GitHub read-back found a required PR rule, admin enforcement enabled, force pushes disabled and deletions disabled. All five required labels already existed: human-gate, blocking, deferred, accepted-risk, not-material. No label mutation was needed. Runner force-push guards are configured and unchanged; enforcement in every native permission mode remains unverified. Project-setup confirmation is bounded to observed forge settings and configured guard presence, consistent with the prior self-adoption report.

Authorization: Dave instructed "adopt fiducial" in this chat. That existing task instruction authorizes this routine installation; no new post-review response is claimed. No contradictions required a new ruling. Human merge remains outstanding under the adopt procedure. The adoption ruling is to be appended to decisions/log.md by the decision session at merge, with its ID allocated then.

Known gaps and boundaries: native fresh-session Claude loading, Codex project trust, and native hook delivery remain unverified/deferred; the user can open a fresh session at /Users/dave/code/fiducial and run /context to verify Claude loading. This evidence does not claim enforcement. Existing #415 (push-readback) is mitigated here by explicit remote SHA read-back; #416 (source-only skill paths) is not-material for this self-adopting repository, where those paths exist. No boundary class changes. SLO/error budget and browser verification are N/A for this metadata change.

Recommendation: ship. Classification: routine; no consequential release gate. Operational effect: source-version provenance only. Rollback: revert this adoption commit through a PR; operative context remains identical either way. Human decision point: merge the adoption PR. Detailed local plan, diff, review, authorization, forge snapshots and verification logs are retained at /private/tmp/fiducial-adopt-20261105T184423Z; this committed report and its review preserve the durable outcome.
