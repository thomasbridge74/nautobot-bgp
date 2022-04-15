from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from .models import ASN, BGPSession, Community, RoutingPolicy, BGPPeerGroup

from .views import (
    ASNListView, ASNView, ASNBulkDeleteView, ASNEditView, ASNBulkEditView,
    ASNDeleteView, CommunityListView, CommunityEditView, CommunityView,
    CommunityBulkEditView, CommunityBulkDeleteView, CommunityDeleteView,
    BGPSessionListView, BGPSessionEditView, BGPSessionBulkDeleteView,
    BGPSessionView, BGPSessionDeleteView, BGPSessionAddView,
    RoutingPolicyListView, RoutingPolicyEditView, RoutingPolicyBulkDeleteView,
    RoutingPolicyView, RoutingPolicyDeleteView, BGPPeerGroupListView,
    BGPPeerGroupEditView, BGPPeerGroupBulkDeleteView, BGPPeerGroupView,
    BGPPeerGroupDeleteView
)

urlpatterns = [
    path('asn/', ASNListView.as_view(), name='asn_list'),
    path('asn/add/', ASNEditView.as_view(), name='asn_add'),
    path('asn/edit/', ASNBulkEditView.as_view(), name='asn_bulk_edit'),
    path('asn/delete/', ASNBulkDeleteView.as_view(), name='asn_bulk_delete'),
    path('asn/<int:pk>/', ASNView.as_view(), name='asn'),
    path('asn/<int:pk>/edit/', ASNEditView.as_view(), name='asn_edit'),
    path('asn/<int:pk>/delete/', ASNDeleteView.as_view(), name='asn_delete'),
    path('asn/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='asn_changelog', kwargs={'model': ASN}),
    # Community
    path('community/', CommunityListView.as_view(), name='community_list'),
    path('community/add/', CommunityEditView.as_view(), name='community_add'),
    path('community/edit/', CommunityBulkEditView.as_view(), name='community_bulk_edit'),
    path('community/delete/', CommunityBulkDeleteView.as_view(), name='community_bulk_delete'),
    path('community/<int:pk>/', CommunityView.as_view(), name='community'),
    path('community/<int:pk>/edit/', CommunityEditView.as_view(), name='community_edit'),
    path('community/<int:pk>/delete/', CommunityDeleteView.as_view(), name='community_delete'),
    path('community/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='community_changelog', kwargs={'model': Community}),
    # Sessions
    path('session/', BGPSessionListView.as_view(), name='bgpsession_list'),
    path('session/add/', BGPSessionAddView.as_view(), name='bgpsession_add'),
    path('session/delete/', BGPSessionBulkDeleteView.as_view(), name='bgpsession_bulk_delete'),
    path('session/<int:pk>/', BGPSessionView.as_view(), name='bgpsession'),
    path('session/<int:pk>/edit/', BGPSessionEditView.as_view(), name='bgpsession_edit'),
    path('session/<int:pk>/delete/', BGPSessionDeleteView.as_view(), name='bgpsession_delete'),
    path('session/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='bgpsession_changelog', kwargs={'model': BGPSession}),
    # Routing Policies
    path('routing-policy/<int:pk>/', RoutingPolicyView.as_view(), name='routingpolicy'),
    path('routing-policy/', RoutingPolicyListView.as_view(), name='routingpolicy_list'),
    path('routing-policy/add/', RoutingPolicyEditView.as_view(), name='routingpolicy_add'),
    path('routing-policy/<int:pk>/edit/', RoutingPolicyEditView.as_view(), name='routingpolicy_edit'),
    path('routing-policy/delete/', RoutingPolicyBulkDeleteView.as_view(), name='routingpolicy_bulk_delete'),
    path('routing-policy/<int:pk>/delete/', RoutingPolicyDeleteView.as_view(), name='routingpolicy_delete'),
    path('routing-policy/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='routingpolicy_changelog', kwargs={'model': RoutingPolicy}),
    # Peer Groups
    path('peer-group/', BGPPeerGroupListView.as_view(), name='bgppeergroup_list'),
    path('peer-group/add/', BGPPeerGroupEditView.as_view(), name='bgppeergroup_add'),
    path('peer-group/delete/', BGPPeerGroupBulkDeleteView.as_view(), name='bgppeergroup_bulk_delete'),
    path('peer-group/<int:pk>/', BGPPeerGroupView.as_view(), name='bgppeergroup'),
    path('peer-group/<int:pk>/edit/', BGPPeerGroupEditView.as_view(), name='bgppeergroup_edit'),
    path('peer-group/<int:pk>/delete/', BGPPeerGroupDeleteView.as_view(), name='bgppeergroup_delete'),
    path('peer-group/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='bgppeergroup_changelog', kwargs={'model': BGPPeerGroup}),
]
