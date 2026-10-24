from enum import StrEnum


class CostGroupDimension(StrEnum):
    BILLINGACCOUNT = "billingAccount"
    CHARGECATEGORY = "chargeCategory"
    CHARGECLASS = "chargeClass"
    CLUSTER = "cluster"
    COMMITMENTSTATUS = "commitmentStatus"
    COMMITMENTTYPE = "commitmentType"
    NAMESPACE = "namespace"
    PRICINGCATEGORY = "pricingCategory"
    PROVIDER = "provider"
    PROVIDERNAME = "providerName"
    REGION = "region"
    RESOURCEID = "resourceId"
    RESOURCENAME = "resourceName"
    SEGMENT = "segment"
    SERVICECATEGORY = "serviceCategory"
    SERVICENAME = "serviceName"
    SERVICESUBCATEGORY = "serviceSubcategory"
    SKU = "sku"
    SUBACCOUNT = "subAccount"
    TAG = "tag"
    TAGGED = "tagged"
    USAGEUNIT = "usageUnit"
    VIRTUALTAG = "virtualTag"

    def __str__(self) -> str:
        return str(self.value)
