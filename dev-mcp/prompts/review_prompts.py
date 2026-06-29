def review_code():
    return """
Review the provided code and provide feedback in the following format:

1. Summary
   - What does the code do?

2. Strengths
   - Good design decisions
   - Readability
   - Maintainability

3. Issues
   - Bugs
   - Edge cases
   - Anti-patterns

4. Recommendations
   - Refactoring suggestions
   - Performance improvements
   - Maintainability improvements

5. Overall Assessment
   - Excellent / Good / Needs Improvement
"""

def security_review():
    return """
Perform a security review of the provided code.

Check for:

1. Path Traversal
2. Command Injection
3. SQL Injection
4. Hardcoded Secrets
5. Unsafe File Access
6. Missing Input Validation
7. Authentication Issues
8. Authorization Issues

Return:

- Risk Level
- Findings
- Recommendations
"""

def summarize_changes():
    return """
Analyze the provided git changes.

Generate:

1. Summary of Changes
2. Files Modified
3. New Features
4. Bug Fixes
5. Breaking Changes
6. Testing Recommendations

Keep the summary concise and suitable for a pull request description.
"""

def generate_test_cases():
    return """
Generate pytest test cases for the provided code.

Requirements:

1. Happy Path Tests
2. Error Handling Tests
3. Edge Cases
4. Security Tests
5. Input Validation Tests

Return complete pytest functions where possible.
"""

def explain_code():
    return """
Explain the provided code to a developer.

Include:

1. Purpose
2. Inputs
3. Outputs
4. Logic Flow
5. Dependencies
6. Potential Improvements

Use simple language suitable for someone learning the codebase.
"""

def refactor_code():
    return """
Refactor the provided code.

Goals:

1. Improve readability
2. Reduce duplication
3. Improve maintainability
4. Follow Python best practices
5. Preserve functionality

Provide:
- Refactored code
- Explanation of changes
"""