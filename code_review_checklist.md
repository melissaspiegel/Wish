# Code Review Checklist

## ✅ 1. Pipeline & Tests
- [ ] **Failing tests?** If any tests fail, investigate the errors before approving.
- [ ] **CI/CD pipeline status?** Ensure all checks and automated tests pass.
- [ ] **Test coverage?** Are there new tests covering the new logic?
- [ ] **Edge cases tested?** Does it handle unexpected input or boundary cases?
- [ ] **Performance considerations?** Are loops, queries, and computations efficient?

## ✅ 2. Merge Request Title & Description
- [ ] **Title follows convention?** (e.g., `feat: add user search` or `fix: resolve auth issue`)
- [ ] **Description is clear?** Explains **what** changed, **why**, and any dependencies.
- [ ] **Linked to a ticket or issue?** (e.g., JIRA, GitHub Issue)
- [ ] **Screenshots (if UI changes)?** Included if there are frontend modifications.

## ✅ 3. Branch & Commit Hygiene
- [ ] **Branch created from the correct source branch?** (e.g., feature branches from `develop`, hotfixes from `main`)
- [ ] **Meaningful commit messages?** Descriptive and follows commit guidelines (e.g., `fix: handle null user ID`).
- [ ] **Commits are atomic?** Small, logical changes rather than one big commit.

## ✅ 4. Code Quality & Formatting
- [ ] **Consistent formatting?** (linting, indentation, spacing)
- [ ] **Follows naming conventions?** (e.g., `camelCase` for JavaScript, `snake_case` for Python)
- [ ] **Avoids hardcoded values?** Uses constants or environment variables.
- [ ] **Removes unnecessary debug logs?** (e.g., `console.log`, `print`, `debugger`)

## ✅ 5. Security & Best Practices
- [ ] **Proper error handling?** No unhandled exceptions.
- [ ] **Prevents SQL Injection & XSS?** If applicable, use parameterized queries and sanitize input.
- [ ] **Avoids storing secrets in code?** Checks for `.env` variables instead.

## ✅ 6. Dependencies & External Calls
- [ ] **Unnecessary dependencies removed?** No unused packages added.
- [ ] **Efficient API/database queries?** Uses pagination, avoids redundant calls.
- [ ] **Third-party libraries validated?** Ensures they are secure and necessary.

## ✅ 7. Documentation & Comments
- [ ] **Code is self-explanatory?** Uses meaningful variable and function names.
- [ ] **Complex logic is documented?** Inline comments where needed.
- [ ] **README updated if required?** If setup or usage instructions changed.

## Final Steps Before Approval
✅ Leave **constructive feedback** (e.g., "This function could be optimized using a set lookup instead of a list.")  
✅ Ask **questions** if something is unclear.  
✅ If everything looks good, **approve the merge request**!  

---

### 🚀 Pro Tip:
If you spot an issue, frame it as **a suggestion** rather than criticism.  
Example:  
❌ _"This function is bad."_  
✅ _"Would it be more efficient to use a dictionary lookup here instead of iterating through the list?"_

---

This checklist ensures you're **thorough, efficient, and professional** in the review.
