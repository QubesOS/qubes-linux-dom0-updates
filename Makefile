FEDORA_MIRROR ?= https://download.fedoraproject.org/pub/fedora/linux
FC28_BASEURL = $(FEDORA_MIRROR)/releases/28/Everything/source/tree/Packages
KEYS = keys/RPM-GPG-KEY-fedora-28-primary

include Makefile.builder

DIST ?= fc25
ALL_URLS := $(addprefix $(FC28_BASEURL)/x/, $(XORG_DRIVERS_FROM_FC28))

ALL_FILES := $(notdir $(ALL_URLS:%.fc28.src.rpm=%.$(DIST).src.rpm))

ifneq ($(DISTFILES_MIRROR),)
ALL_URLS := $(addprefix $(DISTFILES_MIRROR),$(ALL_FILES))
endif

UNTRUSTED_SUFF = .UNTRUSTED

rpmdb/.imported: $(KEYS)
	@mkdir -p rpmdb
	@rpmkeys --dbpath=$(PWD)/rpmdb --import $(KEYS)
	@touch rpmdb/.imported

%.fc28.src.rpm: rpmdb/.imported
	@wget --no-use-server-timestamps -q -O $@$(UNTRUSTED_SUFF) $(filter %/$@,$(ALL_URLS))
	@rpmkeys --dbpath=$(PWD)/rpmdb --checksig $@$(UNTRUSTED_SUFF) | grep 'signatures OK$$\|rsa sha1 (md5) pgp md5 OK$$'
	@mv $@$(UNTRUSTED_SUFF) $@

%.$(DIST).src.rpm: %.fc28.src.rpm
	mv $< $@

.PHONY: get-sources verify-sources
get-sources: $(ALL_FILES)

verify-sources:
	@true
