# -*- mode:python; coding:utf-8 -*-
# Copyright (c) 2020 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
#
####### DO NOT EDIT DO NOT EDIT DO NOT EDIT DO NOT EDIT DO NOT EDIT ######
#                                                                        #
#        This file is automatically generated by gen_oscal.py            #
#                                                                        #
####### DO NOT EDIT DO NOT EDIT DO NOT EDIT DO NOT EDIT DO NOT EDIT ######
#
#
from __future__ import annotations

import re
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, EmailStr, Extra, Field, conint, constr, validator

from trestle.core.base_model import OscalBaseModel
from trestle.oscal import OSCAL_VERSION_REGEX, OSCAL_VERSION
import trestle.oscal.common as common


class Statement(OscalBaseModel):
    """
    Identifies which statements within a control are addressed.
    """

    class Config:
        extra = Extra.forbid

    statement_id: constr(
        regex=
        r'^[_A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD][_A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD\-\.0-9\u00B7\u0300-\u036F\u203F-\u2040]*$'
    ) = Field(
        ...,
        alias='statement-id',
        description='A human-oriented identifier reference to a control statement.',
        title='Control Statement Reference',
    )
    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this control statement elsewhere in this or other OSCAL instances. The UUID of the control statement in the source OSCAL instance is sufficient to reference the data item locally or globally (e.g., in an imported OSCAL instance).',
        title='Control Statement Reference Universally Unique Identifier',
    )
    description: str = Field(
        ...,
        description='A summary of how the containing control statement is implemented by the component or capability.',
        title='Statement Implementation Description',
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    responsible_roles: Optional[List[common.ResponsibleRole]] = Field(None, alias='responsible-roles')
    remarks: Optional[str] = None


class State(Enum):
    """
    The operational status.
    """

    under_development = 'under-development'
    operational = 'operational'
    disposition = 'disposition'
    other = 'other'


class Status(OscalBaseModel):
    """
    Describes the operational status of the system component.
    """

    class Config:
        extra = Extra.forbid

    state: State = Field(..., description='The operational status.', title='State')
    remarks: Optional[str] = None


class SetParameter(OscalBaseModel):
    """
    Identifies the parameter that will be set by the enclosed value.
    """

    class Config:
        extra = Extra.forbid

    param_id: constr(
        regex=
        r'^[_A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD][_A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD\-\.0-9\u00B7\u0300-\u036F\u203F-\u2040]*$'
    ) = Field(
        ...,
        alias='param-id',
        description=
        "A human-oriented reference to a parameter within a control, who's catalog has been imported into the current implementation context.",
        title='Parameter ID',
    )
    values: List[constr(regex=r'^\S(.*\S)?$')] = Field(...)
    remarks: Optional[str] = None


class IncorporatesComponent(OscalBaseModel):
    """
    TBD
    """

    class Config:
        extra = Extra.forbid

    component_uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        alias='component-uuid',
        description='A machine-oriented identifier reference to a component.',
        title='Component Reference',
    )
    description: str = Field(
        ...,
        description='A description of the component, including information about its function.',
        title='Component Description',
    )


class ImportComponentDefinition(OscalBaseModel):
    """
    Loads a component definition from another resource.
    """

    class Config:
        extra = Extra.forbid

    href: str = Field(
        ...,
        description=
        'A link to a resource that defines a set of components and/or capabilities to import into this collection.',
        title='Hyperlink Reference',
    )


class ImplementedRequirement(OscalBaseModel):
    """
    Describes how the containing component or capability implements an individual control.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference a specific control implementation elsewhere in this or other OSCAL instances. The locally defined UUID of the control implementation can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance).This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Control Implementation Identifier',
    )
    control_id: constr(
        regex=
        r'^[_A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD][_A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD\-\.0-9\u00B7\u0300-\u036F\u203F-\u2040]*$'
    ) = Field(
        ...,
        alias='control-id',
        description=
        'A human-oriented identifier reference to a control with a corresponding id value. When referencing an externally defined control, the Control Identifier Reference must be used in the context of the external / imported OSCAL instance (e.g., uri-reference).',
        title='Control Identifier Reference',
    )
    description: str = Field(
        ...,
        description=
        'A suggestion for how the specified control may be implemented if the containing component or capability is instantiated in a system security plan.',
        title='Control Implementation Description',
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    set_parameters: Optional[List[SetParameter]] = Field(None, alias='set-parameters')
    responsible_roles: Optional[List[common.ResponsibleRole]] = Field(None, alias='responsible-roles')
    statements: Optional[List[Statement]] = Field(None)
    remarks: Optional[str] = None


class ControlImplementation(OscalBaseModel):
    """
    Defines how the component or capability supports a set of controls.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference a set of implemented controls elsewhere in this or other OSCAL instances. The locally defined UUID of the control implementation set can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance). This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Control Implementation Set Identifier',
    )
    source: str = Field(
        ...,
        description=
        'A reference to an OSCAL catalog or profile providing the referenced control or subcontrol definition.',
        title='Source Resource Reference',
    )
    description: str = Field(
        ...,
        description=
        'A description of how the specified set of controls are implemented for the containing component or capability.',
        title='Control Implementation Description',
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    set_parameters: Optional[List[SetParameter]] = Field(None, alias='set-parameters')
    implemented_requirements: List[ImplementedRequirement] = Field(..., alias='implemented-requirements')


class Capability(OscalBaseModel):
    """
    A grouping of other components and/or capabilities.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this capability elsewhere in this or other OSCAL instances. The locally defined UUID of the capability can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance).This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Capability Identifier',
    )
    name: constr(regex=r'^\S(.*\S)?$') = Field(
        ...,
        description="The capability's human-readable name.",
        title='Capability Name',
    )
    description: str = Field(..., description='A summary of the capability.', title='Capability Description')
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    incorporates_components: Optional[List[IncorporatesComponent]] = Field(None, alias='incorporates-components')
    control_implementations: Optional[List[ControlImplementation]] = Field(None, alias='control-implementations')
    remarks: Optional[str] = None


class DefinedComponent(OscalBaseModel):
    """
    A defined component that can be part of an implemented system.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this component elsewhere in this or other OSCAL instances. The locally defined UUID of the component can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance). This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Component Identifier',
    )
    type: constr(regex=r'^\S(.*\S)?$') = Field(
        ...,
        description='A category describing the purpose of the component.',
        title='Component Type',
    )
    title: str = Field(
        ...,
        description='A human readable name for the component.',
        title='Component Title',
    )
    description: str = Field(
        ...,
        description='A description of the component, including information about its function.',
        title='Component Description',
    )
    purpose: Optional[str] = Field(
        None,
        description='A summary of the technological or business purpose of the component.',
        title='Purpose',
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    responsible_roles: Optional[List[common.ResponsibleRole]] = Field(None, alias='responsible-roles')
    protocols: Optional[List[common.Protocol]] = Field(None)
    control_implementations: Optional[List[ControlImplementation]] = Field(None, alias='control-implementations')
    remarks: Optional[str] = None


class ComponentDefinition(OscalBaseModel):
    """
    A collection of component descriptions, which may optionally be grouped by capability.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this component definition elsewhere in this or other OSCAL instances. The locally defined UUID of the component definition can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance). This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Component Definition Universally Unique Identifier',
    )
    metadata: common.Metadata
    import_component_definitions: Optional[List[ImportComponentDefinition]] = Field(
        None, alias='import-component-definitions'
    )
    components: Optional[List[DefinedComponent]] = Field(None)
    capabilities: Optional[List[Capability]] = Field(None)
    back_matter: Optional[common.BackMatter] = Field(None, alias='back-matter')


class Model(OscalBaseModel):
    component_definition: ComponentDefinition = Field(..., alias='component-definition')
