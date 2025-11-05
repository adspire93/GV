# Contributing to GammaVantage

Thank you for considering contributing to GammaVantage!

## How to Contribute

### Reporting Bugs

- Use GitHub Issues to report bugs
- Include detailed steps to reproduce
- Provide error messages and logs
- Specify environment (OS, Python version, etc.)

### Suggesting Features

- Open a GitHub Issue with [Feature Request] in title
- Describe the feature and use case
- Explain why it would be valuable

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
   - Follow coding standards (PEP 8)
   - Add docstrings to functions
   - Write unit tests
   - Update documentation

4. **Test your changes**
   ```bash
   pytest tests/
   ```

5. **Commit with clear messages**
   ```bash
   git commit -m "Add: Feature description"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Describe changes clearly
   - Reference related issues
   - Ensure all tests pass

## Coding Standards

### Python Code Style
- Follow PEP 8
- Use type hints
- Maximum line length: 100 characters
- Use meaningful variable names

### Documentation
- Add docstrings to all functions/classes
- Update README.md if needed
- Add comments for complex logic

### Testing
- Write unit tests for new features
- Maintain 80%+ test coverage
- Test edge cases and error conditions

### Commit Messages
Format: `<Type>: <Description>`

Types:
- `Add`: New feature
- `Fix`: Bug fix
- `Update`: Enhancement to existing feature
- `Refactor`: Code refactoring
- `Docs`: Documentation changes
- `Test`: Test additions/changes

Example: `Add: Trade simulator P&L calculation`

## Code Review Process

1. All PRs require review before merging
2. Address reviewer comments
3. Keep PRs focused and small
4. Squash commits before merge

## Questions?

- Open a GitHub Issue
- Email: dev@gammavantage.com

Thank you for contributing! 🙏
