# ~ Variables
# ~~ API
PYVERS = python3.12
VENV = ./.venv
REQUIREMENTS = ./requirements.txt

# ~~ Parameters
ACTIVE = . ./$(VENV)/bin/activate

# ~ Scripts
# ~~ Mandatory
.PHONY: all help help-md autophony venv install info clean
all: help

# ~~ Misc.
help: ## Show this help.
	@grep "##" $(MAKEFILE_LIST) | grep -v "grep" | sed 's/:.*##\s*/:@\t/g' | column -t -s "@"

# ~~ Simple Workflow
dev: check-venv ## Run the API Server on dev mode (with reload).
	@$(ACTIVE) && uvicorn ??? --reload

venv: ## Generate a Python Virtual Environnement.
	@$(PYVERS) -m venv $(VENV)

install: check-venv ## Install all the files in the requirement file.
	@$(ACTIVE) && pip install --upgrade pip setuptools wheel
	@$(ACTIVE) && pip install -r $(REQUIREMENTS)

# ~~ Useful tools
freeze: check-venv ## Update the requirement file.
	@$(ACTIVE) && pip freeze > $(REQUIREMENTS)

info: check-venv ## Display information about the Virtual Environnement.
	@printf "Using Virtual Environnement at '$(VENV)' with " && $(ACTIVE) && python --version

clean: ## Clean all the generated files and folders.
	@find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

# ---------------------
# - Useless for users -
# ---------------------

# check-venv: Returns an error message and quit if the venv folder is not created.
check-venv: 
	@stat $(VENV) > /dev/null 2> /dev/null || (echo "Run \`$$ make venv\` first." && exit 1)

# markdown: Show this help but in a markdown styled way. This can be used when updating the Makefile to generate documentation and simplify README.md's 'Make rules' section update.
markdown: 
	@grep "##" $(MAKEFILE_LIST) | grep -v "grep" | sed -E 's/([^:]*):.*##\s*/- ***\1***:@\t/g' | column -t -s "@"

# autophony: Generate a .PHONY rule for your Makefile using all rules in the Makefile(s).
autophony: 
	@grep -oE "^[a-zA-Z-]*\:" $(MAKEFILE_LIST) | sed "s/://g" | xargs echo ".PHONY:"
