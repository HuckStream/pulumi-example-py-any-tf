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

__all__ = ['UuidArgs', 'Uuid']

@pulumi.input_type
class UuidArgs:
    def __init__(__self__, *,
                 keepers: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a Uuid resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for
               more information.
        """
        if keepers is not None:
            pulumi.set(__self__, "keepers", keepers)

    @property
    @pulumi.getter
    def keepers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for
        more information.
        """
        return pulumi.get(self, "keepers")

    @keepers.setter
    def keepers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "keepers", value)


@pulumi.input_type
class _UuidState:
    def __init__(__self__, *,
                 keepers: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 result: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering Uuid resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for
               more information.
        :param pulumi.Input[builtins.str] result: The generated uuid presented in string format.
        """
        if keepers is not None:
            pulumi.set(__self__, "keepers", keepers)
        if result is not None:
            pulumi.set(__self__, "result", result)

    @property
    @pulumi.getter
    def keepers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for
        more information.
        """
        return pulumi.get(self, "keepers")

    @keepers.setter
    def keepers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "keepers", value)

    @property
    @pulumi.getter
    def result(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The generated uuid presented in string format.
        """
        return pulumi.get(self, "result")

    @result.setter
    def result(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "result", value)


@pulumi.type_token("random:index/uuid:Uuid")
class Uuid(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 keepers: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        Create a Uuid resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for
               more information.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[UuidArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Uuid resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param UuidArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UuidArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 keepers: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UuidArgs.__new__(UuidArgs)

            __props__.__dict__["keepers"] = keepers
            __props__.__dict__["result"] = None
        super(Uuid, __self__).__init__(
            'random:index/uuid:Uuid',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            keepers: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
            result: Optional[pulumi.Input[builtins.str]] = None) -> 'Uuid':
        """
        Get an existing Uuid resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for
               more information.
        :param pulumi.Input[builtins.str] result: The generated uuid presented in string format.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UuidState.__new__(_UuidState)

        __props__.__dict__["keepers"] = keepers
        __props__.__dict__["result"] = result
        return Uuid(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def keepers(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for
        more information.
        """
        return pulumi.get(self, "keepers")

    @property
    @pulumi.getter
    def result(self) -> pulumi.Output[builtins.str]:
        """
        The generated uuid presented in string format.
        """
        return pulumi.get(self, "result")

