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

__all__ = ['AnomalyDetectionArgs', 'AnomalyDetection']

@pulumi.input_type
class AnomalyDetectionArgs:
    def __init__(__self__, *,
                 body: pulumi.Input[builtins.str],
                 anomaly_detection_id: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a AnomalyDetection resource.
        :param pulumi.Input[builtins.str] body: The anomaly detection document
        """
        pulumi.set(__self__, "body", body)
        if anomaly_detection_id is not None:
            pulumi.set(__self__, "anomaly_detection_id", anomaly_detection_id)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Input[builtins.str]:
        """
        The anomaly detection document
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter(name="anomalyDetectionId")
    def anomaly_detection_id(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "anomaly_detection_id")

    @anomaly_detection_id.setter
    def anomaly_detection_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "anomaly_detection_id", value)


@pulumi.input_type
class _AnomalyDetectionState:
    def __init__(__self__, *,
                 anomaly_detection_id: Optional[pulumi.Input[builtins.str]] = None,
                 body: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering AnomalyDetection resources.
        :param pulumi.Input[builtins.str] body: The anomaly detection document
        """
        if anomaly_detection_id is not None:
            pulumi.set(__self__, "anomaly_detection_id", anomaly_detection_id)
        if body is not None:
            pulumi.set(__self__, "body", body)

    @property
    @pulumi.getter(name="anomalyDetectionId")
    def anomaly_detection_id(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "anomaly_detection_id")

    @anomaly_detection_id.setter
    def anomaly_detection_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "anomaly_detection_id", value)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The anomaly detection document
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "body", value)


@pulumi.type_token("opensearch:index/anomalyDetection:AnomalyDetection")
class AnomalyDetection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 anomaly_detection_id: Optional[pulumi.Input[builtins.str]] = None,
                 body: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Create a AnomalyDetection resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] body: The anomaly detection document
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AnomalyDetectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AnomalyDetection resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AnomalyDetectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AnomalyDetectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 anomaly_detection_id: Optional[pulumi.Input[builtins.str]] = None,
                 body: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AnomalyDetectionArgs.__new__(AnomalyDetectionArgs)

            __props__.__dict__["anomaly_detection_id"] = anomaly_detection_id
            if body is None and not opts.urn:
                raise TypeError("Missing required property 'body'")
            __props__.__dict__["body"] = body
        super(AnomalyDetection, __self__).__init__(
            'opensearch:index/anomalyDetection:AnomalyDetection',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            anomaly_detection_id: Optional[pulumi.Input[builtins.str]] = None,
            body: Optional[pulumi.Input[builtins.str]] = None) -> 'AnomalyDetection':
        """
        Get an existing AnomalyDetection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] body: The anomaly detection document
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AnomalyDetectionState.__new__(_AnomalyDetectionState)

        __props__.__dict__["anomaly_detection_id"] = anomaly_detection_id
        __props__.__dict__["body"] = body
        return AnomalyDetection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="anomalyDetectionId")
    def anomaly_detection_id(self) -> pulumi.Output[builtins.str]:
        return pulumi.get(self, "anomaly_detection_id")

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[builtins.str]:
        """
        The anomaly detection document
        """
        return pulumi.get(self, "body")

