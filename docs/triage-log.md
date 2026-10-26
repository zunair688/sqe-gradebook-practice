# Bug Triage Log — v0.2 Grade Statistics

## 1. Purpose

This document records the severity, priority, and sprint decisions for five reported gradebook bugs. The three highest-priority issues will be addressed in the current sprint. The remaining two issues are deferred.

## 2. Issue Prioritization

| Bug | Severity | Priority | Decision |
|---|---|---|---|
| Average crashes when a student has no scores | High | P1 | Fix this sprint |
| Gradebook accepts scores outside 0–100 | High | P1 | Fix this sprint |
| Gradebook allows duplicate roll numbers | Medium | P1 | Fix this sprint |
| Average is not rounded to two decimal places | Low | P3 | Defer |
| Student name search is case-sensitive | Low | P3 | Defer |

Replace the descriptions above with the actual GitHub issue numbers and links after verifying the created issues.

## 3. Severity vs Priority

**Severity** describes the impact of a defect on the system. **Priority** describes how urgently the team should fix it.

The empty-average bug has High severity because requesting an average for a student with no scores causes a runtime exception. It is assigned P1 because the application should handle this normal situation safely.

The duplicate-roll-number bug has Medium severity because duplicate identifiers can create ambiguity between student records. It is assigned P1 because reliable student identification is important for gradebook data integrity.

The average-rounding and case-sensitive-search issues have Low severity and P3 priority. They affect output formatting and search convenience rather than directly causing a crash or corrupting stored marks. They are deferred to a later sprint.

## 4. Current Sprint Scope

The following issues are selected for implementation:

1. Return a safe average when a student has no scores.
2. Reject scores below 0 or above 100.
3. Reject duplicate student roll numbers.

Each fix will be developed on its own branch, tested, and submitted through a pull request.

## 5. Deferred Issues

### Average rounding
Decision: Deferred from the current sprint because it has lower priority than runtime safety and data validation.

### Case-sensitive student search
Decision: Deferred from the current sprint because it is a usability improvement rather than a critical data-integrity fix.

These issues are deferred for this sprint and may be reconsidered in a later milestone.

## 6. Testing and Verification

Each selected fix must have a regression test. The team will run the relevant tests and the full test suite before merging the pull request.

After merging, verify that the linked issue closes automatically and record the test result in the issue discussion.

## 7. Release Readiness

The release will be considered ready for review when the three selected defects are fixed, regression tests pass, and the corresponding pull requests are merged. The two deferred issues will remain documented for future work. Final release readiness depends on successful test results and review of the merged changes.