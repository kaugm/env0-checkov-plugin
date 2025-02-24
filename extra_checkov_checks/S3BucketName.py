from __future__ import annotations

from typing import Any

from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class S3BucketNameStartsWith(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure S3 Bucket name starts with env0"
        id = "CKV_AWS_999"
        supported_resources = ("aws_s3_bucket",)
        # CheckCategories are defined in models/enums.py
        categories = (CheckCategories.BACKUP_AND_RECOVERY,)
        guideline = "TEST RULE NO GUIDELINE"
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources, guideline=guideline)

    def scan_resource_conf(self, conf: dict[str, list[Any]]) -> CheckResult:
        """
        ARBITRARY: CHECKS FOR BUCKET NAME STARTING WITH STRING
        :param conf: aws_s3_bucket configuration
        :return: <CheckResult>
        
        # EXAMPLE
        tags = conf.get("tags")
        if tags and isinstance(tags, list):
            tags = tags[0]
            if tags.get("Scope") == "PCI":
                acl_block = conf['acl']
                if acl_block in [["public-read"], ["public-read-write"], ["website"]]:
                    return CheckResult.FAILED
        return CheckResult.PASSED
        """

	# Test for bucket name starts with
        name = conf.get("bucket")
	print(conf)
	print(name)
	# name = conf['planned_values']['root_module']['resources'][0]['values']['bucket']
        if name[0][:4] == "env0":
        	return CheckResult.PASSED
        return CheckResult.FAILED



check = S3BucketNameStartsWith()
