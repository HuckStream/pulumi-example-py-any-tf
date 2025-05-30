# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
from . import _utilities
import typing
# Export this package's modules as members:
from .anomaly_detection import *
from .audit_config import *
from .channel_configuration import *
from .cluster_settings import *
from .component_template import *
from .composable_index_template import *
from .dashboard_object import *
from .dashboard_tenant import *
from .data_stream import *
from .get_host import *
from .index import *
from .index_template import *
from .ingest_pipeline import *
from .ism_policy import *
from .ism_policy_mapping import *
from .monitor import *
from .provider import *
from .role import *
from .roles_mapping import *
from .script import *
from .sm_policy import *
from .snapshot_repository import *
from .user import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_opensearch.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_opensearch.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "opensearch",
  "mod": "index/anomalyDetection",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/anomalyDetection:AnomalyDetection": "AnomalyDetection"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/auditConfig",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/auditConfig:AuditConfig": "AuditConfig"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/channelConfiguration",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/channelConfiguration:ChannelConfiguration": "ChannelConfiguration"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/clusterSettings",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/clusterSettings:ClusterSettings": "ClusterSettings"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/componentTemplate",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/componentTemplate:ComponentTemplate": "ComponentTemplate"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/composableIndexTemplate",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/composableIndexTemplate:ComposableIndexTemplate": "ComposableIndexTemplate"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/dashboardObject",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/dashboardObject:DashboardObject": "DashboardObject"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/dashboardTenant",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/dashboardTenant:DashboardTenant": "DashboardTenant"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/dataStream",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/dataStream:DataStream": "DataStream"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/index",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/index:Index": "Index"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/indexTemplate",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/indexTemplate:IndexTemplate": "IndexTemplate"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/ingestPipeline",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/ingestPipeline:IngestPipeline": "IngestPipeline"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/ismPolicy",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/ismPolicy:IsmPolicy": "IsmPolicy"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/ismPolicyMapping",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/ismPolicyMapping:IsmPolicyMapping": "IsmPolicyMapping"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/monitor",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/monitor:Monitor": "Monitor"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/role",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/role:Role": "Role"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/rolesMapping",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/rolesMapping:RolesMapping": "RolesMapping"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/script",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/script:Script": "Script"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/smPolicy",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/smPolicy:SmPolicy": "SmPolicy"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/snapshotRepository",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/snapshotRepository:SnapshotRepository": "SnapshotRepository"
  }
 },
 {
  "pkg": "opensearch",
  "mod": "index/user",
  "fqn": "pulumi_opensearch",
  "classes": {
   "opensearch:index/user:User": "User"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "opensearch",
  "token": "pulumi:providers:opensearch",
  "fqn": "pulumi_opensearch",
  "class": "Provider"
 }
]
"""
)
