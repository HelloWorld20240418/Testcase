HOST = "192.168.15.231"
USERNAME = "admin"
PASSWORD = "admin"

CASE_JSON = {
	"_id": "67f4baae85d716e39f81bf04",
	"DisplayName": "HttpCps_client_to_2vm_server",
	"DUTRole": "Server",
	"DutSystemVersion": "Supernova-20C 25.06.09 build5082",
	"ImageVersion": "25.06.09",
	"IPVersion": "v4",
	"MenuMode": "Layer47Test",
	"NetworkConfig": {
		"NetworkControl": {
			"ArpNsnaTimeoutSeconds": 30,
			"BcastNextMacOnlyFirstIP": "no",
			"FlowRatio": "1:1",
			"IPAddLoopPriority": "Client",
			"IPChangeAlgorithm": "Increment",
			"IpPortMapping": "no",
			"IpPortMappingTxt": "",
			"Layer4PacketsCount": "no",
			"Layer4PortAddStep": 1,
			"MaxEventPerLoop": 64,
			"MaxPortDownTime": 10,
			"MaxTimerPerLoop": 16,
			"MessageSyncTimeoutSecond": 30,
			"NetWork": "默认协议栈选项",
			"NetworkCardUpTime": 5,
			"NicPhyRewrite": "yes",
			"Piggybacking": "yes",
			"PingConnectivityCheck": "yes",
			"PingTimeOutSecond": 15,
			"PortChangeAlgorithm": "Random",
			"PromiscuousMode": "no",
			"SendGratuitousArp": "yes",
			"StartClientDelaySecond": 2,
			"StopCloseAgeingSecond": 2,
			"SystemTimerDebug": "no",
			"TCLRunMoment": "start",
			"TcpPerfectClose": "no",
			"TcpStopCloseMethod": "Reset",
			"TcpTimerSchedUsecond": 100,
			"TesterMessagePort": 2002,
			"TimerSchedOutAction": "Warning",
			"TwotierByteStatistics": "no",
			"WaitPortsUpSecond": 30
		},
		"SlaveHost": [
			{
				"Host": "192.168.15.231",
				"Ports": [
					{
						"CoreBind": "2",
						"device": "NetiTest IT2X010GF47LA 1G/10G SmartNIC",
						"GTPUTunnel": {
							"GTPUEnable": "no",
							"GtpuNetworkMask": 16,
							"TunnelIPAddr1": "172.1.1.2",
							"TunnelIPAddr2": "172.1.2.2",
							"TunnelIPVersion": 4,
							"TunnelPort1": 2152,
							"TunnelQfi": 1,
							"TunnelTeid1": 1
						},
						"HeadChecksumConf": {
							"IPV4HeadChecksumType": "auto",
							"TCPHeadChecksumType": "auto",
							"UDPHeadChecksumType": "auto"
						},
						"Interface": "port1",
						"MacMasquerade": "A2:01#disabled",
						"MACSEC": {
							"CAK_NAME": "1",
							"CAK_VALUE": "000102030405060708090a0b0c0d0e0f",
							"macsec_cipher_suite": "gcm-aes-128",
							"macsec_PN": 1,
							"MACSECEnable": "no",
							"PORT_Identifer": 1,
							"SCI_MAC": "001122334455"
						},
						"MsgFragSet": {
							"IPv4FragEnable": "no",
							"IPv4TCPMSS": "1460",
							"IPv4UDPEnable": "no",
							"IPv6FragEnable": "no",
							"IPv6TCPMSS": "100",
							"IPv6UDPEnable": "no",
							"MTUCoverEnable": "no",
							"PccketFragmentDisorder": "no",
							"PccketFragmentHeadpkt": "no",
							"PccketFragmentOverlap": "no",
							"PortMTU": "1500"
						},
						"nb_rxd": 4096,
						"nb_txd": 4096,
						"NetworkSubnets": [
							{
								"Gateway": "#disabled",
								"IpAddrRange": "23.1.1.2",
								"Netmask": "24",
								"ServerAddressFormat": "IP",
								"ServerIPRange": "23.1.1.100",
								"SubnetEnable": "yes",
								"SubnetNumber": "1",
								"SubnetRole": "client",
								"SubnetStep": "0.0.0.1",
								"SubnetVersion": "v4",
								"VlanID": "1#disabled"
							},
							{
								"Gateway": "#disabled",
								"IpAddrRange": "29.0.0.2",
								"Netmask": "24",
								"ServerAddressFormat": "IP",
								"ServerIPRange": "29.0.0.200",
								"SubnetEnable": "yes",
								"SubnetNumber": "2",
								"SubnetRole": "client",
								"SubnetStep": "0.0.0.1",
								"SubnetVersion": "v4",
								"VlanID": "1#disabled"
							}
						],
						"NetworkZone": [
							{
								"NetworkZoneCount": 1,
								"NetworkZoneEnable": "no",
								"NetworkZoneMask": "16",
								"NetworkZoneStart": "17.1.0.0",
								"NetworkZoneStep": "0.1.0.0",
								"SimulatorRouterIPAddr": "0.0.1.2#disabled",
								"SubnetNumber": "1",
								"SubnetVersion": "v4"
							},
							{
								"NetworkZoneCount": 1,
								"NetworkZoneEnable": "no",
								"NetworkZoneMask": "64",
								"NetworkZoneStart": "3ffe:0:17:2::0",
								"NetworkZoneStep": "0:0:0:1::0",
								"SimulatorRouterIPAddr": "0:0:0:1::1:2#disabled",
								"SubnetNumber": "2",
								"SubnetVersion": "v6"
							}
						],
						"NextPortMacMethod": "ARP_NSNA#disabled",
						"nictype": "PERF",
						"OuterVlanID": "1#disabled",
						"PacketCapture": [
							{
								"CaptureMessage": "All",
								"CapturePacketEnable": "no",
								"CaptureProtocol": "None",
								"MgmtIp": "192.168.15.97",
								"PhysicalPort": "port1"
							}
						],
						"PacketFilter": [
							{
								"DstPortMathes": "Eq",
								"FilterAction": "Drop",
								"FilteringIPVersion": "v4",
								"FilteringProtocol": "All",
								"PacketFilterEnable": "no",
								"SrcPortMathes": "Eq"
							}
						],
						"PortEnable": "yes",
						"PortRXRSS": "no",
						"PortSide": "client",
						"PortSpeedDetectMode": "Autoneg",
						"PortSpeedLimit": [
							{
								"Accumulate": "slice_add",
								"FlushTokenUsecond": "1000",
								"LimitGraph": "fixed",
								"LimitMode": "Interface",
								"LimitType": "case",
								"Name": "HttpCps",
								"SpeedLimit": 0,
								"TestType": "HttpCps"
							}
						],
						"PortStreamTemplate": {
							"StreamTemplate": ""
						},
						"QinqType": "0x88A8#disabled",
						"QoSConfiguration": {
							"ECN": "00",
							"IPDscpPriority": "24",
							"PriorityEnable": "DscpBased",
							"RoCEv2PFCList": "0,0,0,1,0,0,0,0",
							"RoCEv2PFCMode": "no",
							"VlanPriority": "3"
						},
						"receivequeue": "4",
						"sendqueue": "4",
						"SimUserSpeedLimit": [
							{
								"Accumulate": "slice_add",
								"FlushTokenUsecond": "1000",
								"IterationRange": 5,
								"IterationStandard": 95,
								"LimitGraph": "fixed",
								"LimitMode": "Interface",
								"LimitType": "simuser",
								"Name": "HttpCps",
								"StabilizeTestTime": 5,
								"TestType": "HttpCps"
							}
						],
						"TesterPortMacAddress": "00:16:31:f2:f3:94#disabled",
						"VirtualRouterConfig": [
							{
								"SubnetNumber": "1",
								"SubnetVersion": "v4",
								"VirtualRouterEnable": "no",
								"VirtualRouterIPAddr": "17.0.0.2",
								"VirtualRouterMask": "16",
								"VirtualRouterNextHop": "17.0.0.1#disabled",
								"VirtualRouterProtocol": "Static"
							},
							{
								"SubnetNumber": "2",
								"SubnetVersion": "v6",
								"VirtualRouterEnable": "no",
								"VirtualRouterIPAddr": "3ffe:0:17:0::1:2",
								"VirtualRouterMask": "64",
								"VirtualRouterNextHop": "3ffe:0:17:0::1:1#disabled",
								"VirtualRouterProtocol": "Static"
							}
						],
						"VlanID": "1#disabled",
						"VXLANTunnel": {
							"DstVTEPIPAddr": "192.168.2.2",
							"SrcVTEPIPAddr": "192.168.1.2",
							"StartVniID": 10,
							"StepVniID": 10,
							"TunnelCount": 1,
							"VlanIDStep": "1#disabled",
							"VniIdCount": 10,
							"VTEPDstMac": "68:91:d0:01:01:01#disabled",
							"VTEPIPNetmask": "16",
							"VTEPIPVersion": 4,
							"VXLANEnable": "no",
							"VXLANVlanID": "1#disabled"
						}
					}
				]
			}
		]
	},
	"Notes": "",
	"ProxyMode": "Reverse",
	"ReportInterval": 1,
	"Specifics": [
		{
			"CaseObject": {
				"FileObject": "get_web",
				"FileObjMapFolder": "67f4b975b2c005e445eab6bf",
				"Monitor": "默认监控器对象Ping",
				"Variate": "无",
				"WebTestProjectId": "67f4b975b2c005e445eab6be",
				"WebTestProjectName": "web_server"
			},
			"ClientProfiles": {
				"Actions": {},
				"ClientCloseMode": "Reset",
				"RequestHeader": [
					"User-Agent: Firefox/41.0"
				],
				"SourcePortRange": "10000-65535"
			},
			"Loads": {
				"CaseAssignMemoryGB": 12,
				"CookieTrafficRatio": 100,
				"DNSQueryTimeOut": 1000,
				"DPDKHugeMemoryPct": 50,
				"HttpLogTraffic": "no",
				"HttpMaxRequest": 0,
				"HttpNewConnReqNum": 0,
				"HttpNewSessionTotal": 0,
				"HttpOverLapMode": "user",
				"HttpPercentageLatencyStat": "no",
				"HttpPipelineEn": "no",
				"HttpRedirectNewTcpEn": "no",
				"HttpRequestHashSize": 512,
				"HttpRequestTimeoutSecond": 10000,
				"HttpThinkTimeMaxCc": 2000000,
				"HttpThinkTimeMode": "fixed",
				"HttpTrafficLogCount": 1000,
				"HttpTranscationStatistics": "yes",
				"HttpWebStatIPNum": 10,
				"MaxThinkTime": 37500,
				"MinThinkTime": 1,
				"NewTcpEachRequrest": "no",
				"OnlyRecordAbnormalResponse": "no",
				"OnlyRecordAssertFailed": "no",
				"SendPktStatEn": "no",
				"SimUser": 600,
				"SimuserFixReq": "no",
				"ThinkTime": 37500,
				"UserApplyMemoryMB": 28
			},
			"ServerProfiles": {
				"DNSServerPort": "53",
				"ResponseHeader": [
					"Server: nginx/1.9.5",
					"Content-Type: text/html"
				],
				"ServerPort": "80"
			},
			"TestType": "HttpCps"
		}
	],
	"TestDuration": 10,
	"TestMode": "TP",
	"TestName": "HttpCps_client_to_2vm_server",
	"TestType": "HttpCps",
	"User": "admin",
	"WorkMode": "Standalone"
}
CASE_JSON_VM = {
	"_id": "67f4bad811bc7dbd92e7f446",
	"DisplayName": "HttpCps_client",
	"DUTRole": "Server",
	"DutSystemVersion": "Supernova-20C 25.06.09 build5082",
	"ImageVersion": "25.06.09",
	"IPVersion": "v4",
	"MenuMode": "Layer47Test",
	"NetworkConfig": {
		"NetworkControl": {
			"ArpNsnaTimeoutSeconds": 30,
			"BcastNextMacOnlyFirstIP": "no",
			"FlowRatio": "1:1",
			"IPAddLoopPriority": "Client",
			"IPChangeAlgorithm": "Increment",
			"IpPortMapping": "no",
			"IpPortMappingTxt": "",
			"Layer4PacketsCount": "no",
			"Layer4PortAddStep": 1,
			"MaxEventPerLoop": 64,
			"MaxPortDownTime": 10,
			"MaxTimerPerLoop": 16,
			"MessageSyncTimeoutSecond": 30,
			"NetWork": "默认协议栈选项",
			"NetworkCardUpTime": 5,
			"NicPhyRewrite": "yes",
			"Piggybacking": "yes",
			"PingConnectivityCheck": "yes",
			"PingTimeOutSecond": 15,
			"PortChangeAlgorithm": "Random",
			"PromiscuousMode": "no",
			"SendGratuitousArp": "yes",
			"StartClientDelaySecond": 2,
			"StopCloseAgeingSecond": 2,
			"SystemTimerDebug": "no",
			"TCLRunMoment": "start",
			"TcpPerfectClose": "no",
			"TcpStopCloseMethod": "Reset",
			"TcpTimerSchedUsecond": 100,
			"TesterMessagePort": 2002,
			"TimerSchedOutAction": "Warning",
			"TwotierByteStatistics": "no",
			"WaitPortsUpSecond": 30
		},
		"SlaveHost": [
			{
				"Host": "192.168.15.231",
				"Ports": [
					{
						"CoreBind": "2",
						"device": "NetiTest IT2X010GF47LA 1G/10G SmartNIC",
						"GTPUTunnel": {
							"GTPUEnable": "no",
							"GtpuNetworkMask": 16,
							"TunnelIPAddr1": "172.1.1.2",
							"TunnelIPAddr2": "172.1.2.2",
							"TunnelIPVersion": 4,
							"TunnelPort1": 2152,
							"TunnelQfi": 1,
							"TunnelTeid1": 1
						},
						"HeadChecksumConf": {
							"IPV4HeadChecksumType": "auto",
							"TCPHeadChecksumType": "auto",
							"UDPHeadChecksumType": "auto"
						},
						"Interface": "port1",
						"MacMasquerade": "A2:01#disabled",
						"MACSEC": {
							"CAK_NAME": "1",
							"CAK_VALUE": "000102030405060708090a0b0c0d0e0f",
							"macsec_cipher_suite": "gcm-aes-128",
							"macsec_PN": 1,
							"MACSECEnable": "no",
							"PORT_Identifer": 1,
							"SCI_MAC": "001122334455"
						},
						"MsgFragSet": {
							"IPv4FragEnable": "no",
							"IPv4TCPMSS": "1460",
							"IPv4UDPEnable": "no",
							"IPv6FragEnable": "no",
							"IPv6TCPMSS": "100",
							"IPv6UDPEnable": "no",
							"MTUCoverEnable": "no",
							"PccketFragmentDisorder": "no",
							"PccketFragmentHeadpkt": "no",
							"PccketFragmentOverlap": "no",
							"PortMTU": "1500"
						},
						"nb_rxd": 4096,
						"nb_txd": 4096,
						"NetworkSubnets": [
							{
								"Gateway": "#disabled",
								"IpAddrRange": "23.1.1.2",
								"Netmask": "24",
								"ServerAddressFormat": "IP",
								"ServerIPRange": "23.1.1.100",
								"SubnetEnable": "yes",
								"SubnetNumber": "1",
								"SubnetRole": "client",
								"SubnetStep": "0.0.0.1",
								"SubnetVersion": "v4",
								"VlanID": "1#disabled"
							},
							{
								"Gateway": "#disabled",
								"IpAddrRange": "3ffe:0:17:1::2:2+100",
								"Netmask": "64",
								"ServerAddressFormat": "IP",
								"ServerIPRange": "3ffe:0:17:1::1:2+10",
								"SubnetEnable": "no",
								"SubnetNumber": "2",
								"SubnetRole": "client",
								"SubnetStep": "::1",
								"SubnetVersion": "v6",
								"VlanID": "1#disabled"
							}
						],
						"NetworkZone": [
							{
								"NetworkZoneCount": 1,
								"NetworkZoneEnable": "no",
								"NetworkZoneMask": "16",
								"NetworkZoneStart": "17.1.0.0",
								"NetworkZoneStep": "0.1.0.0",
								"SimulatorRouterIPAddr": "0.0.1.2#disabled",
								"SubnetNumber": "1",
								"SubnetVersion": "v4"
							},
							{
								"NetworkZoneCount": 1,
								"NetworkZoneEnable": "no",
								"NetworkZoneMask": "64",
								"NetworkZoneStart": "3ffe:0:17:2::0",
								"NetworkZoneStep": "0:0:0:1::0",
								"SimulatorRouterIPAddr": "0:0:0:1::1:2#disabled",
								"SubnetNumber": "2",
								"SubnetVersion": "v6"
							}
						],
						"NextPortMacMethod": "ARP_NSNA#disabled",
						"nictype": "PERF",
						"OuterVlanID": "1#disabled",
						"PacketCapture": [
							{
								"CaptureMessage": "All",
								"CapturePacketEnable": "no",
								"CaptureProtocol": "None",
								"MgmtIp": "192.168.15.97",
								"PhysicalPort": "port1"
							}
						],
						"PacketFilter": [
							{
								"DstPortMathes": "Eq",
								"FilterAction": "Drop",
								"FilteringIPVersion": "v4",
								"FilteringProtocol": "All",
								"PacketFilterEnable": "no",
								"SrcPortMathes": "Eq"
							}
						],
						"PortEnable": "yes",
						"PortRXRSS": "no",
						"PortSide": "client",
						"PortSpeedDetectMode": "Autoneg",
						"PortSpeedLimit": [
							{
								"Accumulate": "slice_add",
								"FlushTokenUsecond": "1000",
								"LimitGraph": "fixed",
								"LimitMode": "Interface",
								"LimitType": "case",
								"Name": "HttpCps",
								"SpeedLimit": 0,
								"TestType": "HttpCps"
							}
						],
						"PortStreamTemplate": {
							"StreamTemplate": ""
						},
						"QinqType": "0x88A8#disabled",
						"QoSConfiguration": {
							"ECN": "00",
							"IPDscpPriority": "24",
							"PriorityEnable": "DscpBased",
							"RoCEv2PFCList": "0,0,0,1,0,0,0,0",
							"RoCEv2PFCMode": "no",
							"VlanPriority": "3"
						},
						"receivequeue": "4",
						"sendqueue": "4",
						"SimUserSpeedLimit": [
							{
								"Accumulate": "slice_add",
								"FlushTokenUsecond": "1000",
								"IterationRange": 5,
								"IterationStandard": 95,
								"LimitGraph": "fixed",
								"LimitMode": "Interface",
								"LimitType": "simuser",
								"Name": "HttpCps",
								"StabilizeTestTime": 5,
								"TestType": "HttpCps"
							}
						],
						"TesterPortMacAddress": "00:16:31:f2:f3:94#disabled",
						"VirtualRouterConfig": [
							{
								"SubnetNumber": "1",
								"SubnetVersion": "v4",
								"VirtualRouterEnable": "no",
								"VirtualRouterIPAddr": "17.0.0.2",
								"VirtualRouterMask": "16",
								"VirtualRouterNextHop": "17.0.0.1#disabled",
								"VirtualRouterProtocol": "Static"
							},
							{
								"SubnetNumber": "2",
								"SubnetVersion": "v6",
								"VirtualRouterEnable": "no",
								"VirtualRouterIPAddr": "3ffe:0:17:0::1:2",
								"VirtualRouterMask": "64",
								"VirtualRouterNextHop": "3ffe:0:17:0::1:1#disabled",
								"VirtualRouterProtocol": "Static"
							}
						],
						"VlanID": "1#disabled",
						"VXLANTunnel": {
							"DstVTEPIPAddr": "192.168.2.2",
							"SrcVTEPIPAddr": "192.168.1.2",
							"StartVniID": 10,
							"StepVniID": 10,
							"TunnelCount": 1,
							"VlanIDStep": "1#disabled",
							"VniIdCount": 10,
							"VTEPDstMac": "68:91:d0:01:01:01#disabled",
							"VTEPIPNetmask": "16",
							"VTEPIPVersion": 4,
							"VXLANEnable": "no",
							"VXLANVlanID": "1#disabled"
						}
					}
				]
			}
		]
	},
	"Notes": "",
	"ProxyMode": "Reverse",
	"ReportInterval": 1,
	"Specifics": [
		{
			"CaseObject": {
				"FileObject": "get_web",
				"FileObjMapFolder": "67f4b975b2c005e445eab6bf",
				"Monitor": "默认监控器对象Ping",
				"Variate": "无",
				"WebTestProjectId": "67f4b975b2c005e445eab6be",
				"WebTestProjectName": "web_server"
			},
			"ClientProfiles": {
				"Actions": {},
				"ClientCloseMode": "Reset",
				"RequestHeader": [
					"User-Agent: Firefox/41.0"
				],
				"SourcePortRange": "10000-65535"
			},
			"Loads": {
				"CaseAssignMemoryGB": 12,
				"CookieTrafficRatio": 100,
				"DNSQueryTimeOut": 1000,
				"DPDKHugeMemoryPct": 50,
				"HttpLogTraffic": "no",
				"HttpMaxRequest": 0,
				"HttpNewConnReqNum": 0,
				"HttpNewSessionTotal": 0,
				"HttpOverLapMode": "user",
				"HttpPercentageLatencyStat": "no",
				"HttpPipelineEn": "no",
				"HttpRedirectNewTcpEn": "no",
				"HttpRequestHashSize": 512,
				"HttpRequestTimeoutSecond": 10000,
				"HttpThinkTimeMaxCc": 2000000,
				"HttpThinkTimeMode": "fixed",
				"HttpTrafficLogCount": 1000,
				"HttpTranscationStatistics": "yes",
				"HttpWebStatIPNum": 10,
				"MaxThinkTime": 37500,
				"MinThinkTime": 1,
				"NewTcpEachRequrest": "no",
				"OnlyRecordAbnormalResponse": "no",
				"OnlyRecordAssertFailed": "no",
				"SendPktStatEn": "no",
				"SimUser": 600,
				"SimuserFixReq": "no",
				"ThinkTime": 37500,
				"UserApplyMemoryMB": 28
			},
			"ServerProfiles": {
				"DNSServerPort": "53",
				"ResponseHeader": [
					"Server: nginx/1.9.5",
					"Content-Type: text/html"
				],
				"ServerPort": "80"
			},
			"TestType": "HttpCps"
		}
	],
	"TestDuration": 10,
	"TestMode": "TP",
	"TestName": "HttpCps_client",
	"TestType": "HttpCps",
	"User": "admin",
	"WorkMode": "Standalone"
}

CASE_CONFIGS = [
    {
        "name": "web_performance",
        "case_json": CASE_JSON,
        "test_type": "HttpCps"
    },
    {
        "name": "virtualization_web_performance",
        "case_json": CASE_JSON_VM,
        "test_type": "HttpCps"
    }
]