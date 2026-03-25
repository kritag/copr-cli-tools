spec ?=
outdir ?= .

SRCDIR := $(CURDIR)/.copr-sources
TOPDIR := $(CURDIR)/.copr-rpmbuild

.PHONY: srpm clean

srpm:
	test -n "$(spec)"
	mkdir -p "$(SRCDIR)" "$(TOPDIR)/BUILD" "$(TOPDIR)/BUILDROOT" "$(TOPDIR)/RPMS" "$(TOPDIR)/SOURCES" "$(TOPDIR)/SPECS" "$(TOPDIR)/SRPMS" "$(outdir)"
	rpmspec -P "$(spec)" | awk '/^Source[0-9]+:/ {print $$2}' | while read -r url; do \
		curl -L --fail --retry 3 -o "$(SRCDIR)/$$(basename "$$url")" "$$url"; \
	done
	rpmbuild -bs "$(spec)" \
		--define "_topdir $(TOPDIR)" \
		--define "_sourcedir $(SRCDIR)" \
		--define "_srcrpmdir $(outdir)"

clean:
	rm -rf "$(SRCDIR)" "$(TOPDIR)"
