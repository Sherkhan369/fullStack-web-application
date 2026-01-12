# Backend Tests

This directory contains the test suite for the backend application organized by testing type:

## Directory Structure

- `unit/` - Unit tests for individual functions, classes, and modules
- `integration/` - Integration tests for API endpoints and database interactions
- `contract/` - Contract tests to verify API compliance with specifications

## Running Tests

To run all tests:
```bash
cd backend
pytest
```

To run specific test types:
```bash
# Unit tests only
pytest tests/unit/

# Integration tests only
# pytest tests/integration/

# Contract tests only
pytest tests/contract/
```

## Test Configuration

- `conftest.py` files contain shared fixtures and configurations for each test category
- Use pytest fixtures to set up test data and mock dependencies
- Follow AAA pattern (Arrange, Act, Assert) for clear test structure