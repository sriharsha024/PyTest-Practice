**PyTest Practice Repository Overview**

This repository contains comprehensive PyTest practice programs and mini test suites, covering everything from PyTest fundamentals to advanced pytest-bdd (Behavior Driven Development).
The project follows a structured learning path and emphasizes real-world testing scenarios, automation best practices, and debugging techniques.

**Key Topics Covered**
**PyTest Fundamentals**

Writing basic test functions

Using assert statements effectively

Testing expected exceptions

Function-based and class-based tests

Understanding PyTest test discovery rules

**Fixtures and Test Setup**

Creating and using fixtures

Fixture scopes (function, class, module, session)

Setup and teardown behavior

Using yield in fixtures

Sharing fixtures via conftest.py

Using request object for dynamic fixture behavior

**Parametrization & Data-Driven Testing**

@pytest.mark.parametrize

Running tests with multiple input combinations

Reading test data from CSV files

Config-driven test execution

Validating multiple outputs efficiently

**Markers & Conditional Test Execution**

Custom markers

Registering markers in pytest.ini

skip and skipif

xfail (expected failures)

Platform-based test skipping

Python version–based conditional execution

**PyTest Customizations**

Custom command-line options using pytest_addoption

Environment-based testing (QA / PROD)

Configuration file parsing

Reusable utility modules

Centralized configuration handling

**PyTest-BDD (Behavior Driven Development)**

Writing .feature files using Gherkin syntax

Using Given / When / Then steps

Binding scenarios using scenarios()

Background steps

Parameterized BDD scenarios

Using conftest.py for shared BDD steps

Tagging scenarios and handling markers

Debugging step resolution errors
