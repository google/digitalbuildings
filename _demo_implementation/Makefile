# Convenience targets. Everything here is also a plain python3 command.
PYTHON ?= python3

.PHONY: help demo validate export test lint ci pin clean

help:
	@echo "make demo      - run the whole walkthrough end to end"
	@echo "make validate  - check the sample site's mappings offline"
	@echo "make export    - write out/building_config.yaml"
	@echo "make test      - run the unit tests"
	@echo "make ci        - run every gate the way CI does"
	@echo "make pin       - print the current ontology digest for ontology_pin.yaml"
	@echo "make clean     - remove generated output"

demo:
	$(PYTHON) -m bms_dbo demo

validate:
	$(PYTHON) -m bms_dbo validate

export:
	$(PYTHON) -m bms_dbo export

test:
	$(PYTHON) -m pytest tests/ -q

ci:
	./ci/validate.sh

pin:
	@$(PYTHON) -c "from bms_dbo.ontology import ontology_digest, default_resources_root; \
	print(ontology_digest(default_resources_root()))"

clean:
	rm -rf out __pycache__ .pytest_cache bms_dbo/__pycache__ tests/__pycache__
