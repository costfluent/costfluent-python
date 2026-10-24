from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_entry_tags_type_0 import CostEntryTagsType0


T = TypeVar("T", bound="CostEntry")


@_attrs_define
class CostEntry:
    """
    Attributes:
        charge_period_start (datetime.date):
        charge_category (str):
        service_name (str):
        billed_cost (str):
        line_item_id (None | str | Unset):
        charge_period_end (datetime.date | None | Unset):
        billing_currency (None | str | Unset):
        service_category (None | str | Unset):
        resource_id (None | str | Unset):
        resource_type (None | str | Unset):
        region_id (None | str | Unset):
        consumed_quantity (float | None | Unset):
        consumed_unit (None | str | Unset):
        tags (CostEntryTagsType0 | None | Unset):
        sub_account_id (None | str | Unset):
        sub_account_name (None | str | Unset):
        sku_id (None | str | Unset):
        effective_cost (None | str | Unset):
        charge_description (None | str | Unset):
        commitment_discount_id (None | str | Unset):
        commitment_discount_type (None | str | Unset):
        resource_name (None | str | Unset):
        region_name (None | str | Unset):
        service_subcategory (None | str | Unset):
        billing_account_id (None | str | Unset):
        list_cost (None | str | Unset):
    """

    charge_period_start: datetime.date
    charge_category: str
    service_name: str
    billed_cost: str
    line_item_id: None | str | Unset = UNSET
    charge_period_end: datetime.date | None | Unset = UNSET
    billing_currency: None | str | Unset = UNSET
    service_category: None | str | Unset = UNSET
    resource_id: None | str | Unset = UNSET
    resource_type: None | str | Unset = UNSET
    region_id: None | str | Unset = UNSET
    consumed_quantity: float | None | Unset = UNSET
    consumed_unit: None | str | Unset = UNSET
    tags: CostEntryTagsType0 | None | Unset = UNSET
    sub_account_id: None | str | Unset = UNSET
    sub_account_name: None | str | Unset = UNSET
    sku_id: None | str | Unset = UNSET
    effective_cost: None | str | Unset = UNSET
    charge_description: None | str | Unset = UNSET
    commitment_discount_id: None | str | Unset = UNSET
    commitment_discount_type: None | str | Unset = UNSET
    resource_name: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    service_subcategory: None | str | Unset = UNSET
    billing_account_id: None | str | Unset = UNSET
    list_cost: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cost_entry_tags_type_0 import CostEntryTagsType0

        charge_period_start = self.charge_period_start.isoformat()

        charge_category = self.charge_category

        service_name = self.service_name

        billed_cost = self.billed_cost

        line_item_id: None | str | Unset
        if isinstance(self.line_item_id, Unset):
            line_item_id = UNSET
        else:
            line_item_id = self.line_item_id

        charge_period_end: None | str | Unset
        if isinstance(self.charge_period_end, Unset):
            charge_period_end = UNSET
        elif isinstance(self.charge_period_end, datetime.date):
            charge_period_end = self.charge_period_end.isoformat()
        else:
            charge_period_end = self.charge_period_end

        billing_currency: None | str | Unset
        if isinstance(self.billing_currency, Unset):
            billing_currency = UNSET
        else:
            billing_currency = self.billing_currency

        service_category: None | str | Unset
        if isinstance(self.service_category, Unset):
            service_category = UNSET
        else:
            service_category = self.service_category

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        resource_type: None | str | Unset
        if isinstance(self.resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = self.resource_type

        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        consumed_quantity: float | None | Unset
        if isinstance(self.consumed_quantity, Unset):
            consumed_quantity = UNSET
        else:
            consumed_quantity = self.consumed_quantity

        consumed_unit: None | str | Unset
        if isinstance(self.consumed_unit, Unset):
            consumed_unit = UNSET
        else:
            consumed_unit = self.consumed_unit

        tags: dict[str, Any] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, CostEntryTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        sub_account_id: None | str | Unset
        if isinstance(self.sub_account_id, Unset):
            sub_account_id = UNSET
        else:
            sub_account_id = self.sub_account_id

        sub_account_name: None | str | Unset
        if isinstance(self.sub_account_name, Unset):
            sub_account_name = UNSET
        else:
            sub_account_name = self.sub_account_name

        sku_id: None | str | Unset
        if isinstance(self.sku_id, Unset):
            sku_id = UNSET
        else:
            sku_id = self.sku_id

        effective_cost: None | str | Unset
        if isinstance(self.effective_cost, Unset):
            effective_cost = UNSET
        else:
            effective_cost = self.effective_cost

        charge_description: None | str | Unset
        if isinstance(self.charge_description, Unset):
            charge_description = UNSET
        else:
            charge_description = self.charge_description

        commitment_discount_id: None | str | Unset
        if isinstance(self.commitment_discount_id, Unset):
            commitment_discount_id = UNSET
        else:
            commitment_discount_id = self.commitment_discount_id

        commitment_discount_type: None | str | Unset
        if isinstance(self.commitment_discount_type, Unset):
            commitment_discount_type = UNSET
        else:
            commitment_discount_type = self.commitment_discount_type

        resource_name: None | str | Unset
        if isinstance(self.resource_name, Unset):
            resource_name = UNSET
        else:
            resource_name = self.resource_name

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        service_subcategory: None | str | Unset
        if isinstance(self.service_subcategory, Unset):
            service_subcategory = UNSET
        else:
            service_subcategory = self.service_subcategory

        billing_account_id: None | str | Unset
        if isinstance(self.billing_account_id, Unset):
            billing_account_id = UNSET
        else:
            billing_account_id = self.billing_account_id

        list_cost: None | str | Unset
        if isinstance(self.list_cost, Unset):
            list_cost = UNSET
        else:
            list_cost = self.list_cost

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "chargePeriodStart": charge_period_start,
                "chargeCategory": charge_category,
                "serviceName": service_name,
                "billedCost": billed_cost,
            }
        )
        if line_item_id is not UNSET:
            field_dict["lineItemId"] = line_item_id
        if charge_period_end is not UNSET:
            field_dict["chargePeriodEnd"] = charge_period_end
        if billing_currency is not UNSET:
            field_dict["billingCurrency"] = billing_currency
        if service_category is not UNSET:
            field_dict["serviceCategory"] = service_category
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if consumed_quantity is not UNSET:
            field_dict["consumedQuantity"] = consumed_quantity
        if consumed_unit is not UNSET:
            field_dict["consumedUnit"] = consumed_unit
        if tags is not UNSET:
            field_dict["tags"] = tags
        if sub_account_id is not UNSET:
            field_dict["subAccountId"] = sub_account_id
        if sub_account_name is not UNSET:
            field_dict["subAccountName"] = sub_account_name
        if sku_id is not UNSET:
            field_dict["skuId"] = sku_id
        if effective_cost is not UNSET:
            field_dict["effectiveCost"] = effective_cost
        if charge_description is not UNSET:
            field_dict["chargeDescription"] = charge_description
        if commitment_discount_id is not UNSET:
            field_dict["commitmentDiscountId"] = commitment_discount_id
        if commitment_discount_type is not UNSET:
            field_dict["commitmentDiscountType"] = commitment_discount_type
        if resource_name is not UNSET:
            field_dict["resourceName"] = resource_name
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if service_subcategory is not UNSET:
            field_dict["serviceSubcategory"] = service_subcategory
        if billing_account_id is not UNSET:
            field_dict["billingAccountId"] = billing_account_id
        if list_cost is not UNSET:
            field_dict["listCost"] = list_cost

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cost_entry_tags_type_0 import CostEntryTagsType0

        d = dict(src_dict)
        charge_period_start = datetime.date.fromisoformat(d.pop("chargePeriodStart"))

        charge_category = d.pop("chargeCategory")

        service_name = d.pop("serviceName")

        billed_cost = d.pop("billedCost")

        def _parse_line_item_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        line_item_id = _parse_line_item_id(d.pop("lineItemId", UNSET))

        def _parse_charge_period_end(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                charge_period_end_type_0 = datetime.date.fromisoformat(data)

                return charge_period_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        charge_period_end = _parse_charge_period_end(d.pop("chargePeriodEnd", UNSET))

        def _parse_billing_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_currency = _parse_billing_currency(d.pop("billingCurrency", UNSET))

        def _parse_service_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_category = _parse_service_category(d.pop("serviceCategory", UNSET))

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        def _parse_resource_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_type = _parse_resource_type(d.pop("resourceType", UNSET))

        def _parse_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_id = _parse_region_id(d.pop("regionId", UNSET))

        def _parse_consumed_quantity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        consumed_quantity = _parse_consumed_quantity(d.pop("consumedQuantity", UNSET))

        def _parse_consumed_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consumed_unit = _parse_consumed_unit(d.pop("consumedUnit", UNSET))

        def _parse_tags(data: object) -> CostEntryTagsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = CostEntryTagsType0.from_dict(data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CostEntryTagsType0 | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_sub_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_account_id = _parse_sub_account_id(d.pop("subAccountId", UNSET))

        def _parse_sub_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_account_name = _parse_sub_account_name(d.pop("subAccountName", UNSET))

        def _parse_sku_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku_id = _parse_sku_id(d.pop("skuId", UNSET))

        def _parse_effective_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        effective_cost = _parse_effective_cost(d.pop("effectiveCost", UNSET))

        def _parse_charge_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        charge_description = _parse_charge_description(
            d.pop("chargeDescription", UNSET)
        )

        def _parse_commitment_discount_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commitment_discount_id = _parse_commitment_discount_id(
            d.pop("commitmentDiscountId", UNSET)
        )

        def _parse_commitment_discount_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commitment_discount_type = _parse_commitment_discount_type(
            d.pop("commitmentDiscountType", UNSET)
        )

        def _parse_resource_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_name = _parse_resource_name(d.pop("resourceName", UNSET))

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        def _parse_service_subcategory(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_subcategory = _parse_service_subcategory(
            d.pop("serviceSubcategory", UNSET)
        )

        def _parse_billing_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_account_id = _parse_billing_account_id(d.pop("billingAccountId", UNSET))

        def _parse_list_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_cost = _parse_list_cost(d.pop("listCost", UNSET))

        cost_entry = cls(
            charge_period_start=charge_period_start,
            charge_category=charge_category,
            service_name=service_name,
            billed_cost=billed_cost,
            line_item_id=line_item_id,
            charge_period_end=charge_period_end,
            billing_currency=billing_currency,
            service_category=service_category,
            resource_id=resource_id,
            resource_type=resource_type,
            region_id=region_id,
            consumed_quantity=consumed_quantity,
            consumed_unit=consumed_unit,
            tags=tags,
            sub_account_id=sub_account_id,
            sub_account_name=sub_account_name,
            sku_id=sku_id,
            effective_cost=effective_cost,
            charge_description=charge_description,
            commitment_discount_id=commitment_discount_id,
            commitment_discount_type=commitment_discount_type,
            resource_name=resource_name,
            region_name=region_name,
            service_subcategory=service_subcategory,
            billing_account_id=billing_account_id,
            list_cost=list_cost,
        )

        return cost_entry
