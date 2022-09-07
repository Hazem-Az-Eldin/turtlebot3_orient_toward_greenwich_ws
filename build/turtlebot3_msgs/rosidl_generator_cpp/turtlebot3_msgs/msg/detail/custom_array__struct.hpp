// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from turtlebot3_msgs:msg/CustomArray.idl
// generated code does not contain a copyright notice

#ifndef TURTLEBOT3_MSGS__MSG__DETAIL__CUSTOM_ARRAY__STRUCT_HPP_
#define TURTLEBOT3_MSGS__MSG__DETAIL__CUSTOM_ARRAY__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__turtlebot3_msgs__msg__CustomArray __attribute__((deprecated))
#else
# define DEPRECATED__turtlebot3_msgs__msg__CustomArray __declspec(deprecated)
#endif

namespace turtlebot3_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CustomArray_
{
  using Type = CustomArray_<ContainerAllocator>;

  explicit CustomArray_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit CustomArray_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _data_type =
    std::vector<float, typename ContainerAllocator::template rebind<float>::other>;
  _data_type data;

  // setters for named parameter idiom
  Type & set__data(
    const std::vector<float, typename ContainerAllocator::template rebind<float>::other> & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    turtlebot3_msgs::msg::CustomArray_<ContainerAllocator> *;
  using ConstRawPtr =
    const turtlebot3_msgs::msg::CustomArray_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<turtlebot3_msgs::msg::CustomArray_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<turtlebot3_msgs::msg::CustomArray_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      turtlebot3_msgs::msg::CustomArray_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<turtlebot3_msgs::msg::CustomArray_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      turtlebot3_msgs::msg::CustomArray_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<turtlebot3_msgs::msg::CustomArray_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<turtlebot3_msgs::msg::CustomArray_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<turtlebot3_msgs::msg::CustomArray_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__turtlebot3_msgs__msg__CustomArray
    std::shared_ptr<turtlebot3_msgs::msg::CustomArray_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__turtlebot3_msgs__msg__CustomArray
    std::shared_ptr<turtlebot3_msgs::msg::CustomArray_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CustomArray_ & other) const
  {
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const CustomArray_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CustomArray_

// alias to use template instance with default allocator
using CustomArray =
  turtlebot3_msgs::msg::CustomArray_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace turtlebot3_msgs

#endif  // TURTLEBOT3_MSGS__MSG__DETAIL__CUSTOM_ARRAY__STRUCT_HPP_
