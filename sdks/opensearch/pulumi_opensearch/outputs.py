# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs

__all__ = [
    'AuditConfigAudit',
    'AuditConfigCompliance',
    'AuditConfigComplianceReadWatchedField',
    'IsmPolicyMappingTimeouts',
    'RoleIndexPermission',
    'RoleTenantPermission',
]

@pulumi.output_type
class AuditConfigAudit(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "disabledRestCategories":
            suggest = "disabled_rest_categories"
        elif key == "disabledTransportCategories":
            suggest = "disabled_transport_categories"
        elif key == "enableRest":
            suggest = "enable_rest"
        elif key == "enableTransport":
            suggest = "enable_transport"
        elif key == "excludeSensitiveHeaders":
            suggest = "exclude_sensitive_headers"
        elif key == "ignoreRequests":
            suggest = "ignore_requests"
        elif key == "ignoreUsers":
            suggest = "ignore_users"
        elif key == "logRequestBody":
            suggest = "log_request_body"
        elif key == "resolveBulkRequests":
            suggest = "resolve_bulk_requests"
        elif key == "resolveIndices":
            suggest = "resolve_indices"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AuditConfigAudit. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AuditConfigAudit.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AuditConfigAudit.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 disabled_rest_categories: Optional[Sequence[builtins.str]] = None,
                 disabled_transport_categories: Optional[Sequence[builtins.str]] = None,
                 enable_rest: Optional[builtins.bool] = None,
                 enable_transport: Optional[builtins.bool] = None,
                 exclude_sensitive_headers: Optional[builtins.bool] = None,
                 ignore_requests: Optional[Sequence[builtins.str]] = None,
                 ignore_users: Optional[Sequence[builtins.str]] = None,
                 log_request_body: Optional[builtins.bool] = None,
                 resolve_bulk_requests: Optional[builtins.bool] = None,
                 resolve_indices: Optional[builtins.bool] = None):
        if disabled_rest_categories is not None:
            pulumi.set(__self__, "disabled_rest_categories", disabled_rest_categories)
        if disabled_transport_categories is not None:
            pulumi.set(__self__, "disabled_transport_categories", disabled_transport_categories)
        if enable_rest is not None:
            pulumi.set(__self__, "enable_rest", enable_rest)
        if enable_transport is not None:
            pulumi.set(__self__, "enable_transport", enable_transport)
        if exclude_sensitive_headers is not None:
            pulumi.set(__self__, "exclude_sensitive_headers", exclude_sensitive_headers)
        if ignore_requests is not None:
            pulumi.set(__self__, "ignore_requests", ignore_requests)
        if ignore_users is not None:
            pulumi.set(__self__, "ignore_users", ignore_users)
        if log_request_body is not None:
            pulumi.set(__self__, "log_request_body", log_request_body)
        if resolve_bulk_requests is not None:
            pulumi.set(__self__, "resolve_bulk_requests", resolve_bulk_requests)
        if resolve_indices is not None:
            pulumi.set(__self__, "resolve_indices", resolve_indices)

    @property
    @pulumi.getter(name="disabledRestCategories")
    def disabled_rest_categories(self) -> Optional[Sequence[builtins.str]]:
        return pulumi.get(self, "disabled_rest_categories")

    @property
    @pulumi.getter(name="disabledTransportCategories")
    def disabled_transport_categories(self) -> Optional[Sequence[builtins.str]]:
        return pulumi.get(self, "disabled_transport_categories")

    @property
    @pulumi.getter(name="enableRest")
    def enable_rest(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "enable_rest")

    @property
    @pulumi.getter(name="enableTransport")
    def enable_transport(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "enable_transport")

    @property
    @pulumi.getter(name="excludeSensitiveHeaders")
    def exclude_sensitive_headers(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "exclude_sensitive_headers")

    @property
    @pulumi.getter(name="ignoreRequests")
    def ignore_requests(self) -> Optional[Sequence[builtins.str]]:
        return pulumi.get(self, "ignore_requests")

    @property
    @pulumi.getter(name="ignoreUsers")
    def ignore_users(self) -> Optional[Sequence[builtins.str]]:
        return pulumi.get(self, "ignore_users")

    @property
    @pulumi.getter(name="logRequestBody")
    def log_request_body(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "log_request_body")

    @property
    @pulumi.getter(name="resolveBulkRequests")
    def resolve_bulk_requests(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "resolve_bulk_requests")

    @property
    @pulumi.getter(name="resolveIndices")
    def resolve_indices(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "resolve_indices")


@pulumi.output_type
class AuditConfigCompliance(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "externalConfig":
            suggest = "external_config"
        elif key == "internalConfig":
            suggest = "internal_config"
        elif key == "readIgnoreUsers":
            suggest = "read_ignore_users"
        elif key == "readMetadataOnly":
            suggest = "read_metadata_only"
        elif key == "readWatchedFields":
            suggest = "read_watched_fields"
        elif key == "writeIgnoreUsers":
            suggest = "write_ignore_users"
        elif key == "writeLogDiffs":
            suggest = "write_log_diffs"
        elif key == "writeMetadataOnly":
            suggest = "write_metadata_only"
        elif key == "writeWatchedIndices":
            suggest = "write_watched_indices"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AuditConfigCompliance. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AuditConfigCompliance.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AuditConfigCompliance.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: Optional[builtins.bool] = None,
                 external_config: Optional[builtins.bool] = None,
                 internal_config: Optional[builtins.bool] = None,
                 read_ignore_users: Optional[Sequence[builtins.str]] = None,
                 read_metadata_only: Optional[builtins.bool] = None,
                 read_watched_fields: Optional[Sequence['outputs.AuditConfigComplianceReadWatchedField']] = None,
                 write_ignore_users: Optional[Sequence[builtins.str]] = None,
                 write_log_diffs: Optional[builtins.bool] = None,
                 write_metadata_only: Optional[builtins.bool] = None,
                 write_watched_indices: Optional[Sequence[builtins.str]] = None):
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if external_config is not None:
            pulumi.set(__self__, "external_config", external_config)
        if internal_config is not None:
            pulumi.set(__self__, "internal_config", internal_config)
        if read_ignore_users is not None:
            pulumi.set(__self__, "read_ignore_users", read_ignore_users)
        if read_metadata_only is not None:
            pulumi.set(__self__, "read_metadata_only", read_metadata_only)
        if read_watched_fields is not None:
            pulumi.set(__self__, "read_watched_fields", read_watched_fields)
        if write_ignore_users is not None:
            pulumi.set(__self__, "write_ignore_users", write_ignore_users)
        if write_log_diffs is not None:
            pulumi.set(__self__, "write_log_diffs", write_log_diffs)
        if write_metadata_only is not None:
            pulumi.set(__self__, "write_metadata_only", write_metadata_only)
        if write_watched_indices is not None:
            pulumi.set(__self__, "write_watched_indices", write_watched_indices)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="externalConfig")
    def external_config(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "external_config")

    @property
    @pulumi.getter(name="internalConfig")
    def internal_config(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "internal_config")

    @property
    @pulumi.getter(name="readIgnoreUsers")
    def read_ignore_users(self) -> Optional[Sequence[builtins.str]]:
        return pulumi.get(self, "read_ignore_users")

    @property
    @pulumi.getter(name="readMetadataOnly")
    def read_metadata_only(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "read_metadata_only")

    @property
    @pulumi.getter(name="readWatchedFields")
    def read_watched_fields(self) -> Optional[Sequence['outputs.AuditConfigComplianceReadWatchedField']]:
        return pulumi.get(self, "read_watched_fields")

    @property
    @pulumi.getter(name="writeIgnoreUsers")
    def write_ignore_users(self) -> Optional[Sequence[builtins.str]]:
        return pulumi.get(self, "write_ignore_users")

    @property
    @pulumi.getter(name="writeLogDiffs")
    def write_log_diffs(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "write_log_diffs")

    @property
    @pulumi.getter(name="writeMetadataOnly")
    def write_metadata_only(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "write_metadata_only")

    @property
    @pulumi.getter(name="writeWatchedIndices")
    def write_watched_indices(self) -> Optional[Sequence[builtins.str]]:
        return pulumi.get(self, "write_watched_indices")


@pulumi.output_type
class AuditConfigComplianceReadWatchedField(dict):
    def __init__(__self__, *,
                 fields: Sequence[builtins.str],
                 index: builtins.str):
        pulumi.set(__self__, "fields", fields)
        pulumi.set(__self__, "index", index)

    @property
    @pulumi.getter
    def fields(self) -> Sequence[builtins.str]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def index(self) -> builtins.str:
        return pulumi.get(self, "index")


@pulumi.output_type
class IsmPolicyMappingTimeouts(dict):
    def __init__(__self__, *,
                 create: Optional[builtins.str] = None,
                 update: Optional[builtins.str] = None):
        if create is not None:
            pulumi.set(__self__, "create", create)
        if update is not None:
            pulumi.set(__self__, "update", update)

    @property
    @pulumi.getter
    def create(self) -> Optional[builtins.str]:
        return pulumi.get(self, "create")

    @property
    @pulumi.getter
    def update(self) -> Optional[builtins.str]:
        return pulumi.get(self, "update")


@pulumi.output_type
class RoleIndexPermission(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowedActions":
            suggest = "allowed_actions"
        elif key == "documentLevelSecurity":
            suggest = "document_level_security"
        elif key == "fieldLevelSecurities":
            suggest = "field_level_securities"
        elif key == "indexPatterns":
            suggest = "index_patterns"
        elif key == "maskedFields":
            suggest = "masked_fields"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RoleIndexPermission. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RoleIndexPermission.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RoleIndexPermission.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allowed_actions: Optional[Sequence[builtins.str]] = None,
                 document_level_security: Optional[builtins.str] = None,
                 field_level_securities: Optional[Sequence[builtins.str]] = None,
                 index_patterns: Optional[Sequence[builtins.str]] = None,
                 masked_fields: Optional[Sequence[builtins.str]] = None):
        """
        :param Sequence[builtins.str] allowed_actions: A list of allowed actions.
        :param builtins.str document_level_security: A selector for document-level security (json formatted using jsonencode).
        :param Sequence[builtins.str] field_level_securities: A list of selectors for field-level security.
        :param Sequence[builtins.str] index_patterns: A list of glob patterns for the index names.
        :param Sequence[builtins.str] masked_fields: A list of masked fields
        """
        if allowed_actions is not None:
            pulumi.set(__self__, "allowed_actions", allowed_actions)
        if document_level_security is not None:
            pulumi.set(__self__, "document_level_security", document_level_security)
        if field_level_securities is not None:
            pulumi.set(__self__, "field_level_securities", field_level_securities)
        if index_patterns is not None:
            pulumi.set(__self__, "index_patterns", index_patterns)
        if masked_fields is not None:
            pulumi.set(__self__, "masked_fields", masked_fields)

    @property
    @pulumi.getter(name="allowedActions")
    def allowed_actions(self) -> Optional[Sequence[builtins.str]]:
        """
        A list of allowed actions.
        """
        return pulumi.get(self, "allowed_actions")

    @property
    @pulumi.getter(name="documentLevelSecurity")
    def document_level_security(self) -> Optional[builtins.str]:
        """
        A selector for document-level security (json formatted using jsonencode).
        """
        return pulumi.get(self, "document_level_security")

    @property
    @pulumi.getter(name="fieldLevelSecurities")
    def field_level_securities(self) -> Optional[Sequence[builtins.str]]:
        """
        A list of selectors for field-level security.
        """
        return pulumi.get(self, "field_level_securities")

    @property
    @pulumi.getter(name="indexPatterns")
    def index_patterns(self) -> Optional[Sequence[builtins.str]]:
        """
        A list of glob patterns for the index names.
        """
        return pulumi.get(self, "index_patterns")

    @property
    @pulumi.getter(name="maskedFields")
    def masked_fields(self) -> Optional[Sequence[builtins.str]]:
        """
        A list of masked fields
        """
        return pulumi.get(self, "masked_fields")


@pulumi.output_type
class RoleTenantPermission(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowedActions":
            suggest = "allowed_actions"
        elif key == "tenantPatterns":
            suggest = "tenant_patterns"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RoleTenantPermission. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RoleTenantPermission.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RoleTenantPermission.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allowed_actions: Optional[Sequence[builtins.str]] = None,
                 tenant_patterns: Optional[Sequence[builtins.str]] = None):
        """
        :param Sequence[builtins.str] allowed_actions: A list of allowed actions.
        :param Sequence[builtins.str] tenant_patterns: A list of glob patterns for the tenant names
        """
        if allowed_actions is not None:
            pulumi.set(__self__, "allowed_actions", allowed_actions)
        if tenant_patterns is not None:
            pulumi.set(__self__, "tenant_patterns", tenant_patterns)

    @property
    @pulumi.getter(name="allowedActions")
    def allowed_actions(self) -> Optional[Sequence[builtins.str]]:
        """
        A list of allowed actions.
        """
        return pulumi.get(self, "allowed_actions")

    @property
    @pulumi.getter(name="tenantPatterns")
    def tenant_patterns(self) -> Optional[Sequence[builtins.str]]:
        """
        A list of glob patterns for the tenant names
        """
        return pulumi.get(self, "tenant_patterns")


