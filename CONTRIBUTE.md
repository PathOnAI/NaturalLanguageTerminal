# How to contribute to NLT
Thank you for your interest in NLT!
Here's a guide to help you contribute to this project.

## 1. Get Started
### Fork the repository

At first, you need to fork this copy and create your own version of repo.

### Clone the repository and install the dependencies.

### Installing dependencies with pip
```bash
pip install -r requirements.txt
```

### Installing pre-commit
We strongly recommend installing [pre-commit](https://pre-commit.com/) to ensure proper formatting during development

## 2. Developing and Testing
### Create a branch

Create a new branch for developing your creative features

```shell
git checkout -b your-feature
```

### Make changes and testing

You can develop new features and then you need to make sure everything works as expected. Run our provided tests and make sure the existing ones go well. Your new tests are encouraged.

## 3. Submitting Changes

### Code format check
Please ensure your code is formatted correctly using pre-commit

### Git commit format
We strongly recommend your git commit follows the format below
```bash
git commit -m <type>: <subject>
```

| <type> | <subject>                                     |
|-------------|--------------------------------------------------|
| `feat`      | Add new features                                 |
| `fix`       | Fix bugs                                         |
| `docs`      | Modify documents like README, CONTRIBUTE         |
| `style`     | Modify code format like space and comma without changing code logic |
| `refactor`  | Refactor code structure without adding new features or fixing new bugs |
| `perf`      | Improve performance or user experience                              |
| `test`      | Test features, including unit test and integration test |
| `chore`     | Change the build procedure or add dependencies   |
| `revert`    | Revert to the previous version                   |

### Create a Pull Request

1. Visit your forked NaturalLanguageTerminal repository on GitHub and click the "Compare & pull request" button to initiate the process of submitting your changes to the original repository for review and potential merging.
2. Choose the base branch and the compare branch (your feature branch).💡 Note that when you add new features, it is recommended to choose the (`dev`) branch and if your change does not affect original functions, you may consider choosing the (`main`) branch.
3. Write a title and describe your changes in the description. And it is recommended to select the label of the change to make it more clear.


## 4. Style Guide

This is the style guide determining how code should be formatted. As more code is added, this documentation will be updated.

### Line Length

Each line should not exceed 80 characters.

### Spaces
Each function or class is to have a space between the line and any preceding code if it is not directly associated with the function or class. For example:
```py
# this is a useful comment for the bar function

def foo():
    pass
```

## 5. Review and Approval
Our maintainers will have a review of that and might give some suggestions or ask for more details. After they approve, your commitment can be incorporated into NLT!

If you need some ideas on what to get started with, take a look at our goals for the rest of this year in [issues](https://github.com/PathOnAI/NaturalLanguageTerminal/issues).