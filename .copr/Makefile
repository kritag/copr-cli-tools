spec ?=
outdir ?= .

SRCDIR := $(CURDIR)/.copr-sources
TOPDIR := $(CURDIR)/.copr-rpmbuild

.PHONY: srpm clean

srpm:
	test -n "$(spec)"
	mkdir -p "$(SRCDIR)" "$(TOPDIR)/BUILD" "$(TOPDIR)/BUILDROOT" "$(TOPDIR)/RPMS" "$(TOPDIR)/SOURCES" "$(TOPDIR)/SPECS" "$(TOPDIR)/SRPMS" "$(outdir)"
	rpmspec -P "$(spec)" | awk '/^Source[0-9]+:/ {print $$2}' | while read -r url; do \
		if echo "$$url" | grep -q '://'; then \
			curl -L --fail --retry 3 -o "$(SRCDIR)/$$(basename "$$url")" "$$url"; \
		else \
			cp "$(dir $(spec))$$url" "$(SRCDIR)/$$url"; \
		fi; \
	done
	rpmbuild -bs "$(spec)" \
		--define "_topdir $(TOPDIR)" \
		--define "_sourcedir $(SRCDIR)" \
		--define "_srcrpmdir $(outdir)"

clean:
	rm -rf "$(SRCDIR)" "$(TOPDIR)"
