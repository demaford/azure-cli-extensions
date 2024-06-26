# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AgentConfigurationMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Name of configuration mode to use. Modes are pre-defined configurations of security controls,
    extension allowlists and guest configuration, maintained by Microsoft.
    """

    FULL = "full"
    MONITOR = "monitor"

class AssessmentModeTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the assessment mode.
    """

    IMAGE_DEFAULT = "ImageDefault"
    AUTOMATIC_BY_PLATFORM = "AutomaticByPlatform"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class InstanceViewTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    INSTANCE_VIEW = "instanceView"

class LastAttemptStatusEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the status of Agent Upgrade.
    """

    SUCCESS = "Success"
    FAILED = "Failed"

class OsType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The operating system type of the machine.
    """

    WINDOWS = "Windows"
    LINUX = "Linux"

class PatchModeTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the patch mode.
    """

    IMAGE_DEFAULT = "ImageDefault"
    AUTOMATIC_BY_PLATFORM = "AutomaticByPlatform"
    AUTOMATIC_BY_OS = "AutomaticByOS"
    MANUAL = "Manual"

class PatchOperationStartedBy(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates if operation was triggered by user or by platform.
    """

    USER = "User"
    PLATFORM = "Platform"

class PatchOperationStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The overall success or failure status of the operation. It remains "InProgress" until the
    operation completes. At that point it will become "Unknown", "Failed", "Succeeded", or
    "CompletedWithWarnings."
    """

    UNKNOWN = "Unknown"
    IN_PROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    COMPLETED_WITH_WARNINGS = "CompletedWithWarnings"

class PatchServiceUsed(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the patch service used for the operation.
    """

    UNKNOWN = "Unknown"
    WU = "WU"
    WU_WSUS = "WU_WSUS"
    YUM = "YUM"
    APT = "APT"
    ZYPPER = "Zypper"

class PrivateCloudKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates which kind of VM fabric the instance is an instance of, such as HCI or SCVMM etc.
    """

    AVS = "AVS"
    HCI = "HCI"
    SCVMM = "SCVMM"
    V_MWARE = "VMware"

class PublicNetworkAccessType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The network access policy to determine if Azure Arc agents can use public Azure Arc service
    endpoints. Defaults to disabled (access to Azure Arc services only via private link).
    """

    #: Allows Azure Arc agents to communicate with Azure Arc services over both public (internet) and
    #: private endpoints.
    ENABLED = "Enabled"
    #: Does not allow Azure Arc agents to communicate with Azure Arc services over public (internet)
    #: endpoints. The agents must use the private link.
    DISABLED = "Disabled"

class StatusLevelTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The level code.
    """

    INFO = "Info"
    WARNING = "Warning"
    ERROR = "Error"

class StatusTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the hybrid machine agent.
    """

    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    ERROR = "Error"

class VMGuestPatchClassificationLinux(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    CRITICAL = "Critical"
    SECURITY = "Security"
    OTHER = "Other"

class VMGuestPatchClassificationWindows(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    CRITICAL = "Critical"
    SECURITY = "Security"
    UPDATE_ROLL_UP = "UpdateRollUp"
    FEATURE_PACK = "FeaturePack"
    SERVICE_PACK = "ServicePack"
    DEFINITION = "Definition"
    TOOLS = "Tools"
    UPDATES = "Updates"

class VMGuestPatchRebootSetting(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Defines when it is acceptable to reboot a VM during a software update operation.
    """

    IF_REQUIRED = "IfRequired"
    NEVER = "Never"
    ALWAYS = "Always"

class VMGuestPatchRebootStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The reboot state of the VM following completion of the operation.
    """

    UNKNOWN = "Unknown"
    NOT_NEEDED = "NotNeeded"
    REQUIRED = "Required"
    STARTED = "Started"
    FAILED = "Failed"
    COMPLETED = "Completed"
