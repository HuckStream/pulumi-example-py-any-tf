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

__all__ = [
    'GetHostResult',
    'AwaitableGetHostResult',
    'get_host',
    'get_host_output',
]

@pulumi.output_type
class GetHostResult:
    """
    A collection of values returned by getHost.
    """
    def __init__(__self__, active=None, id=None, url=None):
        if active and not isinstance(active, bool):
            raise TypeError("Expected argument 'active' to be a bool")
        pulumi.set(__self__, "active", active)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def active(self) -> builtins.bool:
        return pulumi.get(self, "active")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def url(self) -> builtins.str:
        return pulumi.get(self, "url")


class AwaitableGetHostResult(GetHostResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHostResult(
            active=self.active,
            id=self.id,
            url=self.url)


def get_host(active: Optional[builtins.bool] = None,
             id: Optional[builtins.str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHostResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['active'] = active
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('opensearch:index/getHost:getHost', __args__, opts=opts, typ=GetHostResult, package_ref=_utilities.get_package()).value

    return AwaitableGetHostResult(
        active=pulumi.get(__ret__, 'active'),
        id=pulumi.get(__ret__, 'id'),
        url=pulumi.get(__ret__, 'url'))
def get_host_output(active: Optional[pulumi.Input[builtins.bool]] = None,
                    id: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetHostResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['active'] = active
    __args__['id'] = id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('opensearch:index/getHost:getHost', __args__, opts=opts, typ=GetHostResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetHostResult(
        active=pulumi.get(__response__, 'active'),
        id=pulumi.get(__response__, 'id'),
        url=pulumi.get(__response__, 'url')))
