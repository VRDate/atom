# Copyright (c) 2011 The Chromium Embedded Framework Authors. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.

{
  'includes': [
    # Bring in the autogenerated source file lists.
    'cef_paths.gypi',
   ],
  'variables': {
    'includes_common': [
      'cef/include/cef_base.h',
      'cef/include/cef_pack_resources.h',
      'cef/include/cef_pack_strings.h',
      'cef/include/cef_runnable.h',
      'cef/include/cef_version.h',
      'cef/include/internal/cef_build.h',
      'cef/include/internal/cef_export.h',
      'cef/include/internal/cef_ptr.h',
      'cef/include/internal/cef_string.h',
      'cef/include/internal/cef_string_list.h',
      'cef/include/internal/cef_string_map.h',
      'cef/include/internal/cef_string_multimap.h',
      'cef/include/internal/cef_string_types.h',
      'cef/include/internal/cef_string_wrappers.h',
      'cef/include/internal/cef_time.h',
      'cef/include/internal/cef_tuple.h',
      'cef/include/internal/cef_types.h',
      'cef/include/internal/cef_types_wrappers.h',
      '<@(autogen_cpp_includes)',
    ],
    'includes_capi': [
      'cef/include/capi/cef_base_capi.h',
      '<@(autogen_capi_includes)',
    ],
    'includes_wrapper': [
      'cef/include/wrapper/cef_byte_read_handler.h',
      'cef/include/wrapper/cef_stream_resource_handler.h',
      'cef/include/wrapper/cef_xml_object.h',
      'cef/include/wrapper/cef_zip_archive.h',
    ],
    'includes_win': [
      'cef/include/internal/cef_types_win.h',
      'cef/include/internal/cef_win.h',
    ],
    'includes_mac': [
      'cef/include/cef_application_mac.h',
      'cef/include/internal/cef_mac.h',
      'cef/include/internal/cef_types_mac.h',
    ],
    'includes_linux': [
      'cef/include/internal/cef_linux.h',
      'cef/include/internal/cef_types_linux.h',
    ],
    'libcef_sources_common': [
      'cef/libcef_dll/cef_logging.h',
      'cef/libcef_dll/cpptoc/cpptoc.h',
      'cef/libcef_dll/ctocpp/ctocpp.h',
      'cef/libcef_dll/libcef_dll.cc',
      'cef/libcef_dll/libcef_dll2.cc',
      'cef/libcef_dll/resource.h',
      'cef/libcef_dll/transfer_util.cpp',
      'cef/libcef_dll/transfer_util.h',
      '<@(autogen_library_side)',
    ],
    'libcef_dll_wrapper_sources_common': [
      'cef/libcef_dll/cef_logging.h',
      'cef/libcef_dll/cpptoc/base_cpptoc.h',
      'cef/libcef_dll/cpptoc/cpptoc.h',
      'cef/libcef_dll/ctocpp/base_ctocpp.h',
      'cef/libcef_dll/ctocpp/ctocpp.h',
      'cef/libcef_dll/transfer_util.cpp',
      'cef/libcef_dll/transfer_util.h',
      'cef/libcef_dll/wrapper/cef_byte_read_handler.cc',
      'cef/libcef_dll/wrapper/cef_stream_resource_handler.cc',
      'cef/libcef_dll/wrapper/cef_xml_object.cc',
      'cef/libcef_dll/wrapper/cef_zip_archive.cc',
      'cef/libcef_dll/wrapper/libcef_dll_wrapper.cc',
      'cef/libcef_dll/wrapper/libcef_dll_wrapper2.cc',
      '<@(autogen_client_side)',
    ],
    'cefclient_sources_common': [
      'tests/cefclient/cefclient.cpp',
      'tests/cefclient/cefclient.h',
      'tests/cefclient/binding_test.cpp',
      'tests/cefclient/binding_test.h',
      'tests/cefclient/client_app.cpp',
      'tests/cefclient/client_app.h',
      'tests/cefclient/client_app_delegates.cpp',
      'tests/cefclient/client_handler.cpp',
      'tests/cefclient/client_handler.h',
      'tests/cefclient/client_renderer.cpp',
      'tests/cefclient/client_renderer.h',
      'tests/cefclient/client_switches.cpp',
      'tests/cefclient/client_switches.h',
      'tests/cefclient/dom_test.cpp',
      'tests/cefclient/dom_test.h',
      'tests/cefclient/res/binding.html',
      'tests/cefclient/res/dialogs.html',
      'tests/cefclient/res/domaccess.html',
      'tests/cefclient/res/localstorage.html',
      'tests/cefclient/res/logo.png',
      'tests/cefclient/res/xmlhttprequest.html',
      'tests/cefclient/resource_util.h',
      'tests/cefclient/scheme_test.cpp',
      'tests/cefclient/scheme_test.h',
      'tests/cefclient/string_util.cpp',
      'tests/cefclient/string_util.h',
      'tests/cefclient/util.h',
    ],
    'cefclient_sources_win': [
      'tests/cefclient/cefclient.rc',
      'tests/cefclient/cefclient_win.cpp',
      'tests/cefclient/client_handler_win.cpp',
      'tests/cefclient/resource.h',
      'tests/cefclient/res/cefclient.ico',
      'tests/cefclient/res/logoball.png',
      'tests/cefclient/res/small.ico',
      'tests/cefclient/resource_util_win.cpp',
    ],
    'cefclient_sources_mac': [
      'tests/cefclient/cefclient_mac.mm',
      'tests/cefclient/client_handler_mac.mm',
      'tests/cefclient/resource_util_mac.mm',
    ],
    'cefclient_sources_mac_helper': [
      'tests/cefclient/binding_test.cpp',
      'tests/cefclient/binding_test.h',
      'tests/cefclient/client_app.cpp',
      'tests/cefclient/client_app.h',
      'tests/cefclient/client_app_delegates.cpp',
      'tests/cefclient/client_handler.cpp',
      'tests/cefclient/client_handler.h',
      'tests/cefclient/client_handler_mac.mm',
      'tests/cefclient/client_renderer.cpp',
      'tests/cefclient/client_renderer.h',
      'tests/cefclient/client_switches.cpp',
      'tests/cefclient/client_switches.h',
      'tests/cefclient/dom_test.cpp',
      'tests/cefclient/dom_test.h',
      'tests/cefclient/process_helper_mac.cpp',
      'tests/cefclient/resource_util.h',
      'tests/cefclient/resource_util_mac.mm',
      'tests/cefclient/scheme_test.cpp',
      'tests/cefclient/scheme_test.h',
      'tests/cefclient/string_util.cpp',
      'tests/cefclient/string_util.h',
      'tests/cefclient/util.h',
    ],
    'cefclient_bundle_resources_mac': [
      'tests/cefclient/mac/cefclient.icns',
      'tests/cefclient/mac/English.lproj/InfoPlist.strings',
      'tests/cefclient/mac/English.lproj/MainMenu.xib',
      'tests/cefclient/mac/Info.plist',
      'tests/cefclient/res/binding.html',
      'tests/cefclient/res/dialogs.html',
      'tests/cefclient/res/domaccess.html',
      'tests/cefclient/res/localstorage.html',
      'tests/cefclient/res/logo.png',
      'tests/cefclient/res/xmlhttprequest.html',
    ],
    'cefclient_sources_linux': [
      'tests/cefclient/cefclient_gtk.cpp',
      'tests/cefclient/client_handler_gtk.cpp',
      'tests/cefclient/resource_util_linux.cpp',
    ],
    'cefclient_bundle_resources_linux': [
      'tests/cefclient/res/binding.html',
      'tests/cefclient/res/dialogs.html',
      'tests/cefclient/res/domaccess.html',
      'tests/cefclient/res/localstorage.html',
      'tests/cefclient/res/logo.png',
      'tests/cefclient/res/xmlhttprequest.html',
    ],
  },
}
