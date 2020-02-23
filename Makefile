FEDORA_MIRROR ?= https://archives.fedoraproject.org/pub/archive/fedora/linux
FC28_BASEURL = $(FEDORA_MIRROR)/releases/28/Everything/source/tree/Packages
FC28_UPDATES_BASEURL = $(FEDORA_MIRROR)/updates/28/Everything/SRPMS/Packages
FC25_BASEURL = $(FEDORA_MIRROR)/releases/25/Everything/source/tree/Packages
FC25_UPDATES_BASEURL = $(FEDORA_MIRROR)/updates/25/SRPMS/Packages
KEYS = keys/RPM-GPG-KEY-fedora-28-primary keys/RPM-GPG-KEY-fedora-25-primary

include Makefile.builder

ALL_URLS := $(foreach pkg,$(PACKAGES_FROM_FC28), \
				$(if $(findstring $(pkg), $(PACKAGES_FROM_FC28_UPDATES)), \
					$(FC28_UPDATES_BASEURL), $(FC28_BASEURL))/$(shell echo $(pkg)|head -c 1|tr A-Z a-z)/$(pkg)) \
            $(foreach pkg,$(PACKAGES_FROM_FC25), \
				$(if $(findstring $(pkg), $(PACKAGES_FROM_FC25_UPDATES)), \
					$(FC25_UPDATES_BASEURL), $(FC25_BASEURL))/$(shell echo $(pkg)|head -c 1|tr A-Z a-z)/$(pkg))

ALL_ORIG_FILES := $(notdir $(ALL_URLS))
ALL_FILES := $(ALL_ORIG_FILES:%.fc28.src.rpm=%.fc25.src.rpm)

ifneq ($(DISTFILES_MIRROR),)
ALL_URLS := $(addprefix $(DISTFILES_MIRROR),$(ALL_FILES))
endif

UNTRUSTED_SUFF = .UNTRUSTED

rpmdb/.imported: $(KEYS)
	@mkdir -p rpmdb
	@rpmkeys --dbpath=$(PWD)/rpmdb --import $(KEYS)
	@touch rpmdb/.imported

$(ALL_ORIG_FILES): %.src.rpm: rpmdb/.imported
	@wget --no-use-server-timestamps -q -O $@$(UNTRUSTED_SUFF) $(filter %/$@,$(ALL_URLS))
	@rpmkeys --dbpath=$(PWD)/rpmdb --checksig $@$(UNTRUSTED_SUFF) | grep 'signatures OK$$\|rsa sha1 (md5) pgp md5 OK$$'
	@mv $@$(UNTRUSTED_SUFF) $@

%.fc25.src.rpm: %.fc28.src.rpm
	mv $< $@

.PHONY: get-sources verify-sources
get-sources: $(ALL_FILES)

verify-sources:
	@true
