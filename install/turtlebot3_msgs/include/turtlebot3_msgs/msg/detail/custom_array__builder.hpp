// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from turtlebot3_msgs:msg/CustomArray.idl
// generated code does not contain a copyright notice

#ifndef TURTLEBOT3_MSGS__MSG__DETAIL__CUSTOM_ARRAY__BUILDER_HPP_
#define TURTLEBOT3_MSGS__MSG__DETAIL__CUSTOM_ARRAY__BUILDER_HPP_

#include "turtlebot3_msgs/msg/detail/custom_array__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace turtlebot3_msgs
{

namespace msg
{

namespace builder
{

class Init_CustomArray_data
{
public:
  Init_CustomArray_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::turtlebot3_msgs::msg::CustomArray data(::turtlebot3_msgs::msg::CustomArray::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot3_msgs::msg::CustomArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot3_msgs::msg::CustomArray>()
{
  return turtlebot3_msgs::msg::builder::Init_CustomArray_data();
}

}  // namespace turtlebot3_msgs

#endif  // TURTLEBOT3_MSGS__MSG__DETAIL__CUSTOM_ARRAY__BUILDER_HPP_
