// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from turtlebot3_msgs:msg/CustomArray.idl
// generated code does not contain a copyright notice

#ifndef TURTLEBOT3_MSGS__MSG__DETAIL__CUSTOM_ARRAY__STRUCT_H_
#define TURTLEBOT3_MSGS__MSG__DETAIL__CUSTOM_ARRAY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'data'
#include "rosidl_runtime_c/primitives_sequence.h"

// Struct defined in msg/CustomArray in the package turtlebot3_msgs.
typedef struct turtlebot3_msgs__msg__CustomArray
{
  rosidl_runtime_c__float__Sequence data;
} turtlebot3_msgs__msg__CustomArray;

// Struct for a sequence of turtlebot3_msgs__msg__CustomArray.
typedef struct turtlebot3_msgs__msg__CustomArray__Sequence
{
  turtlebot3_msgs__msg__CustomArray * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot3_msgs__msg__CustomArray__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TURTLEBOT3_MSGS__MSG__DETAIL__CUSTOM_ARRAY__STRUCT_H_
