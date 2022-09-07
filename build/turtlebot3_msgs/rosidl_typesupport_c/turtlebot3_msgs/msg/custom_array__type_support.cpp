// generated from rosidl_typesupport_c/resource/idl__type_support.cpp.em
// with input from turtlebot3_msgs:msg/CustomArray.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "turtlebot3_msgs/msg/rosidl_typesupport_c__visibility_control.h"
#include "turtlebot3_msgs/msg/detail/custom_array__struct.h"
#include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/message_type_support_dispatch.h"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_c/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace turtlebot3_msgs
{

namespace msg
{

namespace rosidl_typesupport_c
{

typedef struct _CustomArray_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _CustomArray_type_support_ids_t;

static const _CustomArray_type_support_ids_t _CustomArray_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _CustomArray_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _CustomArray_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _CustomArray_type_support_symbol_names_t _CustomArray_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, turtlebot3_msgs, msg, CustomArray)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, turtlebot3_msgs, msg, CustomArray)),
  }
};

typedef struct _CustomArray_type_support_data_t
{
  void * data[2];
} _CustomArray_type_support_data_t;

static _CustomArray_type_support_data_t _CustomArray_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _CustomArray_message_typesupport_map = {
  2,
  "turtlebot3_msgs",
  &_CustomArray_message_typesupport_ids.typesupport_identifier[0],
  &_CustomArray_message_typesupport_symbol_names.symbol_name[0],
  &_CustomArray_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t CustomArray_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_CustomArray_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace msg

}  // namespace turtlebot3_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_turtlebot3_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, turtlebot3_msgs, msg, CustomArray)() {
  return &::turtlebot3_msgs::msg::rosidl_typesupport_c::CustomArray_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
