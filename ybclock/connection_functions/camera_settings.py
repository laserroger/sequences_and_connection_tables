'''
    Cameras have attributes, or settings, you can change in NI MAX.
    **pynivision** allows one to edit these attributes, and labscript allows them to be specified in a simple dictionary format.
    They are programed in order. In python 3.7+, dictionaries have order now.
'''

#camera attributes ran during an experiment!
shot_camera_attributes = {
    'AcquisitionAttributes::AdvancedEthernet::BandwidthControl::DesiredPeakBandwidth': 1000.0,
    'AcquisitionAttributes::AdvancedEthernet::Controller::DestinationMode': 'Unicast',
    'AcquisitionAttributes::AdvancedEthernet::Controller::DestinationMulticastAddress': '239.192.0.1',
    'AcquisitionAttributes::AdvancedEthernet::EventParameters::EventsEnabled': 1,
    'AcquisitionAttributes::AdvancedEthernet::EventParameters::MaxOutstandingEvents': 50,
    'AcquisitionAttributes::AdvancedEthernet::FirewallTraversal::Enabled': 0,
    'AcquisitionAttributes::AdvancedEthernet::FirewallTraversal::KeepAliveTime': 30,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::MaxResendsPerPacket': 25,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::MemoryWindowSize': 1024,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::MissingPacketTimeout': 2,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::NewPacketTimeout': 100,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendBatchingPercentage': 10,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendResponseTimeout': 2,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendThresholdPercentage': 5,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendTimerResolution': 1,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendsEnabled': 1,
    'AcquisitionAttributes::AdvancedEthernet::TestPacketParameters::MaxTestPacketRetries': 1,
    'AcquisitionAttributes::AdvancedEthernet::TestPacketParameters::TestPacketEnabled': 1,
    'AcquisitionAttributes::AdvancedEthernet::TestPacketParameters::TestPacketTimeout': 250,
    'AcquisitionAttributes::AdvancedGenicam::CommandTimeout': 100,
    'AcquisitionAttributes::AdvancedGenicam::IgnoreCameraValidationErrors': 0,
    'AcquisitionAttributes::Bayer::Algorithm': 'Bilinear',
    'AcquisitionAttributes::Bayer::GainB': 1.0,
    'AcquisitionAttributes::Bayer::GainG': 1.0,
    'AcquisitionAttributes::Bayer::GainR': 1.0,
    'AcquisitionAttributes::Bayer::Pattern': 'Use hardware value',
    'AcquisitionAttributes::BitsPerPixel': 'Use hardware value',
    'AcquisitionAttributes::ChunkDataDecoding::ChunkDataDecodingEnabled': 0,
    'AcquisitionAttributes::ChunkDataDecoding::MaximumChunkCopySize': 64,
    'AcquisitionAttributes::ImageDecoderCopyMode': 'Auto',
    'AcquisitionAttributes::IncompleteBufferMode': 'Ignore',
    'AcquisitionAttributes::OutputImageType': 'Auto',
    'AcquisitionAttributes::OverwriteMode': 'Get Newest',
    'AcquisitionAttributes::PacketSize': 1000,
    'AcquisitionAttributes::ReceiveTimestampMode': 'None',
    'AcquisitionAttributes::ShiftPixelBits': 0,
    'AcquisitionAttributes::SwapPixelBytes': 0,
    'AcquisitionAttributes::Timeout': 5000,
    'CameraAttributes::AcquisitionControl::AcquisitionFrameRateEnable': 0,
    'CameraAttributes::AcquisitionControl::AcquisitionMode': 'Continuous',
    'CameraAttributes::AcquisitionControl::ExposureMode': 'Timed',
    'CameraAttributes::AcquisitionControl::ExposureTime': 10000.0,
    'CameraAttributes::AcquisitionControl::TriggerActivation': 'Rising Edge',
    'CameraAttributes::AcquisitionControl::TriggerDelay': 0.0,
    'CameraAttributes::AcquisitionControl::TriggerMode': 'On',
    'CameraAttributes::AcquisitionControl::TriggerOverlap': 'Read Out',
    'CameraAttributes::AcquisitionControl::TriggerSelector': 'Frame Start',
    'CameraAttributes::AcquisitionControl::TriggerSource': 'All',
    'CameraAttributes::ActionControl::ActionGroupKey': 0,
    'CameraAttributes::ActionControl::ActionGroupMask': 0,
    'CameraAttributes::ActionControl::ActionSelector': 0,
    'CameraAttributes::AnalogControl::BlackLevelRaw': 0,
    'CameraAttributes::AnalogControl::BlackLevelSelector': 'All',
    'CameraAttributes::AnalogControl::Gain': 25.021019421142473,
    'CameraAttributes::AnalogControl::GainSelector': 'All',
    'CameraAttributes::BoSequencerControl::BoSequencerEnable': 'Off',
    'CameraAttributes::ChunkDataControl::ChunkGainSelector': 'All',
    'CameraAttributes::ChunkDataControl::ChunkModeActive': 0,
    'CameraAttributes::ChunkDataControl::ChunkSelector': 'BaumerImageHeader3',
    'CameraAttributes::CounterAndTimerControl::FrameCounter': 564920,
    'CameraAttributes::CounterAndTimerControl::TimerDelay': 0.0,
    'CameraAttributes::CounterAndTimerControl::TimerDuration': 100.0,
    'CameraAttributes::CounterAndTimerControl::TimerSelector': 'Timer 1',
    'CameraAttributes::CounterAndTimerControl::TimerTriggerActivation': 'Rising Edge',
    'CameraAttributes::CounterAndTimerControl::TimerTriggerSource': 'Off',
    'CameraAttributes::DeviceControl::DeviceUserID': ' cam1',
    'CameraAttributes::DigitalIOControl::LineDebouncerHighTimeAbs': 0.0,
    'CameraAttributes::DigitalIOControl::LineDebouncerLowTimeAbs': 0.0,
    'CameraAttributes::DigitalIOControl::LineInverter': 0,
    'CameraAttributes::DigitalIOControl::LineSelector': 'Line 0',
    'CameraAttributes::DigitalIOControl::UserOutputSelector': 'User Output 1',
    'CameraAttributes::DigitalIOControl::UserOutputValue': 0,
    'CameraAttributes::DigitalIOControl::UserOutputValueAll': 0,
    'CameraAttributes::EventControl::EventNotification': 'Off',
    'CameraAttributes::EventControl::EventSelector': 'Primary Application Switch',
    'CameraAttributes::ImageFormatControl::BinningHorizontal': 1,
    'CameraAttributes::ImageFormatControl::BinningVertical': 1,
    'CameraAttributes::ImageFormatControl::Height': 490,
    'CameraAttributes::ImageFormatControl::OffsetX': 0,
    'CameraAttributes::ImageFormatControl::OffsetY': 0,
    'CameraAttributes::ImageFormatControl::PixelFormat': 'Mono 8',
    'CameraAttributes::ImageFormatControl::ReverseX': 0,
    'CameraAttributes::ImageFormatControl::TestImageSelector': 'Off',
    'CameraAttributes::ImageFormatControl::Width': 656,
    'CameraAttributes::LUTControl::DefectPixelCorrection': 1,
    'CameraAttributes::LUTControl::DefectPixelListEntryActive': 1,
    'CameraAttributes::LUTControl::DefectPixelListEntryPosX': 389,
    'CameraAttributes::LUTControl::DefectPixelListEntryPosY': 463,
    'CameraAttributes::LUTControl::DefectPixelListIndex': 0,
    'CameraAttributes::LUTControl::LUTEnable': 0,
    'CameraAttributes::LUTControl::LUTIndex': 0,
    'CameraAttributes::LUTControl::LUTSelector': 'Luminance',
    'CameraAttributes::LUTControl::LUTValue': 0,
    'CameraAttributes::TransportLayerControl::GevGVCPHeartbeatDisable': 0,
    'CameraAttributes::TransportLayerControl::GevGVCPPendingAck': 0,
    'CameraAttributes::TransportLayerControl::GevSCFTD': 0,
    'CameraAttributes::TransportLayerControl::GevSupportedOptionSelector': 'IPConfiguration LLA',
    'CameraAttributes::UserSetControl::UserSetDefaultSelector': 'Default',
    'CameraAttributes::UserSetControl::UserSetSelector': 'Default',
}

#camera attributes when not running an experiment!
manual_camera_attributes = {
    'CameraAttributes::AcquisitionControl::AcquisitionFrameRateEnable': 0,
    'CameraAttributes::AcquisitionControl::AcquisitionMode': 'Continuous',
    'CameraAttributes::AcquisitionControl::ExposureMode': 'Timed',
    'CameraAttributes::AcquisitionControl::ExposureTime': 10000.0,
    'CameraAttributes::AcquisitionControl::TriggerActivation': 'Rising Edge',
    'CameraAttributes::AcquisitionControl::TriggerDelay': 0.0,
    'CameraAttributes::AcquisitionControl::TriggerMode': 'Off',
    'CameraAttributes::AcquisitionControl::TriggerOverlap': 'Read Out',
    'CameraAttributes::AcquisitionControl::TriggerSelector': 'Frame Start',
    'CameraAttributes::AcquisitionControl::TriggerSource': 'All',
    'CameraAttributes::ActionControl::ActionGroupKey': 0,
    'CameraAttributes::ActionControl::ActionGroupMask': 0,
    'CameraAttributes::ActionControl::ActionSelector': 0,
    'CameraAttributes::AnalogControl::BlackLevelRaw': 0,
    'CameraAttributes::AnalogControl::BlackLevelSelector': 'All',
    'CameraAttributes::AnalogControl::Gain': 25.021019421142473,
    'CameraAttributes::AnalogControl::GainSelector': 'All',
    'CameraAttributes::BoSequencerControl::BoSequencerEnable': 'Off',
    'CameraAttributes::ChunkDataControl::ChunkGainSelector': 'All',
    'CameraAttributes::ChunkDataControl::ChunkModeActive': 0,
    'CameraAttributes::ChunkDataControl::ChunkSelector': 'BaumerImageHeader3',
    'CameraAttributes::CounterAndTimerControl::FrameCounter': 564920,
    'CameraAttributes::CounterAndTimerControl::TimerDelay': 0.0,
    'CameraAttributes::CounterAndTimerControl::TimerDuration': 100.0,
    'CameraAttributes::CounterAndTimerControl::TimerSelector': 'Timer 1',
    'CameraAttributes::CounterAndTimerControl::TimerTriggerActivation': 'Rising Edge',
    'CameraAttributes::CounterAndTimerControl::TimerTriggerSource': 'Off',
    'CameraAttributes::DeviceControl::DeviceUserID': ' cam1',
    'CameraAttributes::DigitalIOControl::LineDebouncerHighTimeAbs': 0.0,
    'CameraAttributes::DigitalIOControl::LineDebouncerLowTimeAbs': 0.0,
    'CameraAttributes::DigitalIOControl::LineInverter': 0,
    'CameraAttributes::DigitalIOControl::LineSelector': 'Line 0',
    'CameraAttributes::DigitalIOControl::UserOutputSelector': 'User Output 1',
    'CameraAttributes::DigitalIOControl::UserOutputValue': 0,
    'CameraAttributes::DigitalIOControl::UserOutputValueAll': 0,
    'CameraAttributes::EventControl::EventNotification': 'Off',
    'CameraAttributes::EventControl::EventSelector': 'Primary Application Switch',
    'CameraAttributes::ImageFormatControl::BinningHorizontal': 1,
    'CameraAttributes::ImageFormatControl::BinningVertical': 1,
    'CameraAttributes::ImageFormatControl::Height': 490,
    'CameraAttributes::ImageFormatControl::OffsetX': 0,
    'CameraAttributes::ImageFormatControl::OffsetY': 0,
    'CameraAttributes::ImageFormatControl::PixelFormat': 'Mono 8',
    'CameraAttributes::ImageFormatControl::ReverseX': 0,
    'CameraAttributes::ImageFormatControl::TestImageSelector': 'Off',
    'CameraAttributes::ImageFormatControl::Width': 656,
    'CameraAttributes::LUTControl::DefectPixelCorrection': 1,
    'CameraAttributes::LUTControl::DefectPixelListEntryActive': 1,
    'CameraAttributes::LUTControl::DefectPixelListEntryPosX': 389,
    'CameraAttributes::LUTControl::DefectPixelListEntryPosY': 463,
    'CameraAttributes::LUTControl::DefectPixelListIndex': 0,
    'CameraAttributes::LUTControl::LUTEnable': 0,
    'CameraAttributes::LUTControl::LUTIndex': 0,
    'CameraAttributes::LUTControl::LUTSelector': 'Luminance',
    'CameraAttributes::LUTControl::LUTValue': 0,
    'CameraAttributes::TransportLayerControl::GevGVCPHeartbeatDisable': 0,
    'CameraAttributes::TransportLayerControl::GevGVCPPendingAck': 0,
    'CameraAttributes::TransportLayerControl::GevSCFTD': 0,
    'CameraAttributes::TransportLayerControl::GevSupportedOptionSelector': 'IPConfiguration LLA',
    'CameraAttributes::UserSetControl::UserSetDefaultSelector': 'Default',
    'CameraAttributes::UserSetControl::UserSetSelector': 'Default',
}

example_camera_attributes = {
    'AcquisitionAttributes::AdvancedEthernet::BandwidthControl::DesiredPeakBandwidth': 1000.0,
    'AcquisitionAttributes::AdvancedEthernet::Controller::DestinationMode': 'Unicast',
    'AcquisitionAttributes::AdvancedEthernet::Controller::DestinationMulticastAddress': '239.192.0.1',
    'AcquisitionAttributes::AdvancedEthernet::EventParameters::EventsEnabled': 1,
    'AcquisitionAttributes::AdvancedEthernet::EventParameters::MaxOutstandingEvents': 50,
    'AcquisitionAttributes::AdvancedEthernet::FirewallTraversal::Enabled': 0,
    'AcquisitionAttributes::AdvancedEthernet::FirewallTraversal::KeepAliveTime': 30,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::MaxResendsPerPacket': 25,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::MemoryWindowSize': 1024,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::MissingPacketTimeout': 2,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::NewPacketTimeout': 100,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendBatchingPercentage': 10,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendResponseTimeout': 2,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendThresholdPercentage': 5,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendTimerResolution': 1,
    'AcquisitionAttributes::AdvancedEthernet::ResendParameters::ResendsEnabled': 1,
    'AcquisitionAttributes::AdvancedEthernet::TestPacketParameters::MaxTestPacketRetries': 1,
    'AcquisitionAttributes::AdvancedEthernet::TestPacketParameters::TestPacketEnabled': 1,
    'AcquisitionAttributes::AdvancedEthernet::TestPacketParameters::TestPacketTimeout': 250,
    'AcquisitionAttributes::AdvancedGenicam::CommandTimeout': 100,
    'AcquisitionAttributes::AdvancedGenicam::IgnoreCameraValidationErrors': 0,
    'AcquisitionAttributes::Bayer::Algorithm': 'Bilinear',
    'AcquisitionAttributes::Bayer::GainB': 1.0,
    'AcquisitionAttributes::Bayer::GainG': 1.0,
    'AcquisitionAttributes::Bayer::GainR': 1.0,
    'AcquisitionAttributes::Bayer::Pattern': 'Use hardware value',
    'AcquisitionAttributes::BitsPerPixel': 'Use hardware value',
    'AcquisitionAttributes::ChunkDataDecoding::ChunkDataDecodingEnabled': 0,
    'AcquisitionAttributes::ChunkDataDecoding::MaximumChunkCopySize': 64,
    'AcquisitionAttributes::ImageDecoderCopyMode': 'Auto',
    'AcquisitionAttributes::IncompleteBufferMode': 'Ignore',
    'AcquisitionAttributes::OutputImageType': 'Auto',
    'AcquisitionAttributes::OverwriteMode': 'Get Newest',
    'AcquisitionAttributes::PacketSize': 1000,
    'AcquisitionAttributes::ReceiveTimestampMode': 'None',
    'AcquisitionAttributes::ShiftPixelBits': 0,
    'AcquisitionAttributes::SwapPixelBytes': 0,
    'AcquisitionAttributes::Timeout': 5000,
    'CameraAttributes::AcquisitionControl::AcquisitionFrameRateEnable': 0,
    'CameraAttributes::AcquisitionControl::AcquisitionMode': 'Continuous',
    'CameraAttributes::AcquisitionControl::ExposureMode': 'Timed',
    'CameraAttributes::AcquisitionControl::ExposureTime': 10000.0,
    'CameraAttributes::AcquisitionControl::TriggerActivation': 'Rising Edge',
    'CameraAttributes::AcquisitionControl::TriggerDelay': 0.0,
    'CameraAttributes::AcquisitionControl::TriggerMode': 'Off',
    'CameraAttributes::AcquisitionControl::TriggerOverlap': 'Read Out',
    'CameraAttributes::AcquisitionControl::TriggerSelector': 'Frame Start',
    'CameraAttributes::AcquisitionControl::TriggerSource': 'All',
    'CameraAttributes::ActionControl::ActionGroupKey': 0,
    'CameraAttributes::ActionControl::ActionGroupMask': 0,
    'CameraAttributes::ActionControl::ActionSelector': 0,
    'CameraAttributes::AnalogControl::BlackLevelRaw': 0,
    'CameraAttributes::AnalogControl::BlackLevelSelector': 'All',
    'CameraAttributes::AnalogControl::Gain': 25.021019421142473,
    'CameraAttributes::AnalogControl::GainSelector': 'All',
    'CameraAttributes::BoSequencerControl::BoSequencerEnable': 'Off',
    'CameraAttributes::ChunkDataControl::ChunkGainSelector': 'All',
    'CameraAttributes::ChunkDataControl::ChunkModeActive': 0,
    'CameraAttributes::ChunkDataControl::ChunkSelector': 'BaumerImageHeader3',
    'CameraAttributes::CounterAndTimerControl::FrameCounter': 564920,
    'CameraAttributes::CounterAndTimerControl::TimerDelay': 0.0,
    'CameraAttributes::CounterAndTimerControl::TimerDuration': 100.0,
    'CameraAttributes::CounterAndTimerControl::TimerSelector': 'Timer 1',
    'CameraAttributes::CounterAndTimerControl::TimerTriggerActivation': 'Rising Edge',
    'CameraAttributes::CounterAndTimerControl::TimerTriggerSource': 'Off',
    'CameraAttributes::DeviceControl::DeviceUserID': ' cam1',
    'CameraAttributes::DigitalIOControl::LineDebouncerHighTimeAbs': 0.0,
    'CameraAttributes::DigitalIOControl::LineDebouncerLowTimeAbs': 0.0,
    'CameraAttributes::DigitalIOControl::LineInverter': 0,
    'CameraAttributes::DigitalIOControl::LineSelector': 'Line 0',
    'CameraAttributes::DigitalIOControl::UserOutputSelector': 'User Output 1',
    'CameraAttributes::DigitalIOControl::UserOutputValue': 0,
    'CameraAttributes::DigitalIOControl::UserOutputValueAll': 0,
    'CameraAttributes::EventControl::EventNotification': 'Off',
    'CameraAttributes::EventControl::EventSelector': 'Primary Application Switch',
    'CameraAttributes::ImageFormatControl::BinningHorizontal': 1,
    'CameraAttributes::ImageFormatControl::BinningVertical': 1,
    'CameraAttributes::ImageFormatControl::Height': 490,
    'CameraAttributes::ImageFormatControl::OffsetX': 0,
    'CameraAttributes::ImageFormatControl::OffsetY': 0,
    'CameraAttributes::ImageFormatControl::PixelFormat': 'Mono 8',
    'CameraAttributes::ImageFormatControl::ReverseX': 0,
    'CameraAttributes::ImageFormatControl::TestImageSelector': 'Off',
    'CameraAttributes::ImageFormatControl::Width': 656,
    'CameraAttributes::LUTControl::DefectPixelCorrection': 1,
    'CameraAttributes::LUTControl::DefectPixelListEntryActive': 1,
    'CameraAttributes::LUTControl::DefectPixelListEntryPosX': 389,
    'CameraAttributes::LUTControl::DefectPixelListEntryPosY': 463,
    'CameraAttributes::LUTControl::DefectPixelListIndex': 0,
    'CameraAttributes::LUTControl::LUTEnable': 0,
    'CameraAttributes::LUTControl::LUTIndex': 0,
    'CameraAttributes::LUTControl::LUTSelector': 'Luminance',
    'CameraAttributes::LUTControl::LUTValue': 0,
    'CameraAttributes::TransportLayerControl::GevGVCPHeartbeatDisable': 0,
    'CameraAttributes::TransportLayerControl::GevGVCPPendingAck': 0,
    'CameraAttributes::TransportLayerControl::GevSCFTD': 0,
    'CameraAttributes::TransportLayerControl::GevSupportedOptionSelector': 'IPConfiguration LLA',
    'CameraAttributes::UserSetControl::UserSetDefaultSelector': 'Default',
    'CameraAttributes::UserSetControl::UserSetSelector': 'Default',
}