---
id: sandbox-existing-vpc
parent: sandbox-aws-cloudformation
created: 2026-08-29T21:10:00Z
priority: 1
status: done
---

# Sandbox template accepts an existing VPC and subnet instead of creating new ones

AWS limits VPCs to 5 per region by default. Teams spinning up multiple sandboxes hit this quickly.

## Success Criteria

- `ExistingVpcId` parameter exists, type `String`, default empty string
- `ExistingSubnetId` parameter exists, type `String`, default empty string
- When both parameters are provided, no VPC, InternetGateway, VPCGatewayAttachment, PublicSubnet, RouteTable, PublicRoute, or SubnetRouteTableAssociation resources are created
- When both parameters are omitted (empty), all network resources are created exactly as before — no behavior change from current template
- Security group's `VpcId` references the existing VPC when provided, the created VPC otherwise
- Instance's `SubnetId` references the existing subnet when provided, the created subnet otherwise
- Providing `ExistingVpcId` without `ExistingSubnetId` (or vice versa) causes a stack creation failure with a clear error, not a silent misconfiguration

**Note:** The existing subnet must already have a route to an Internet Gateway and `MapPublicIpOnLaunch` enabled, or the instance will not be reachable. This is the caller's responsibility — the template does not validate it.
