# SQE Gradebook — Workflow Notes

## Change Workflow: Idea to Release

The following workflow describes how a change moves from an initial idea to a released feature or fix. A QA engineer contributes throughout the process to help ensure quality, testability, and reliability.

```text
Idea
  |
  v
Issue
  |  QA: Clarify requirements and define acceptance criteria.
  v
Branch
  |  QA: Identify test scenarios and potential risks.
  v
Pull Request (PR)
  |  QA: Check test coverage and verify linked issues.
  v
Review
  |  QA: Review test results, edge cases, and quality concerns.
  v
Merge
  |  QA: Confirm required reviews and checks are satisfied.
  v
CI (Continuous Integration)
  |  QA: Examine automated test results and investigate failures.
  v
Release
     QA: Perform release verification and smoke testing.
```

## QA Engineer Responsibilities

- Issue: Ensure requirements are clear, complete, and testable.
- Branch: Plan relevant test cases, including negative and boundary cases.
- PR: Verify that appropriate tests and documentation accompany the change.
- Review: Examine changes for risks, missing tests, and possible regressions.
- Merge: Confirm that required approvals and available quality checks have passed.
- CI: Monitor automated tests and report failures or unexpected behavior.
- Release: Validate the released change and perform smoke or regression testing as appropriate.

## Reflection

QA is not limited to testing after development is complete. It is a continuous activity that begins when requirements are discussed and continues through code review, integration, and release. Early QA involvement helps identify ambiguity and defects before they become more expensive to fix. CI provides repeatable automated feedback, while release verification checks that the delivered change behaves as expected.

> Note: CI may run before and after merging depending on repository configuration. Release should follow the project's defined quality gates.