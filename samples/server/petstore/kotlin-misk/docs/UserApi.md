# UserApi

All URIs are relative to *http://petstore.swagger.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUser**](UserApi.md#createUser) | **Post** /user | Create user
[**createUsersWithArrayInput**](UserApi.md#createUsersWithArrayInput) | **Post** /user/createWithArray | Creates list of users with given input array
[**createUsersWithListInput**](UserApi.md#createUsersWithListInput) | **Post** /user/createWithList | Creates list of users with given input array
[**deleteUser**](UserApi.md#deleteUser) | **Delete** /user/{username} | Delete user
[**getUserByName**](UserApi.md#getUserByName) | **Get** /user/{username} | Get user by user name
[**loginUser**](UserApi.md#loginUser) | **Get** /user/login | Logs user into the system
[**logoutUser**](UserApi.md#logoutUser) | **Get** /user/logout | Logs out current logged in user session
[**updateUser**](UserApi.md#updateUser) | **Put** /user/{username} | Updated user


<a name="createUser"></a>
# **createUser**
> createUser(user)

Create user

This can only be done by the logged in user.

### Example
```kotlin
// Import classes:
//import org.openapitools.infrastructure.*
//import org.openapitools.server.api.model.*

val apiInstance = UserApi()
val user : User =  // User | Created user object
try {
    apiInstance.createUser(user)
} catch (e: ClientException) {
    println("4xx response calling UserApi#createUser")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UserApi#createUser")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| Created user object |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: APPLICATION_JSON
 - **Accept**: Not defined

<a name="createUsersWithArrayInput"></a>
# **createUsersWithArrayInput**
> createUsersWithArrayInput(user)

Creates list of users with given input array



### Example
```kotlin
// Import classes:
//import org.openapitools.infrastructure.*
//import org.openapitools.server.api.model.*

val apiInstance = UserApi()
val user : kotlin.collections.List<User> =  // kotlin.collections.List<User> | List of user object
try {
    apiInstance.createUsersWithArrayInput(user)
} catch (e: ClientException) {
    println("4xx response calling UserApi#createUsersWithArrayInput")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UserApi#createUsersWithArrayInput")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**kotlin.collections.List&lt;User&gt;**](User.md)| List of user object |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: APPLICATION_JSON
 - **Accept**: Not defined

<a name="createUsersWithListInput"></a>
# **createUsersWithListInput**
> createUsersWithListInput(user)

Creates list of users with given input array



### Example
```kotlin
// Import classes:
//import org.openapitools.infrastructure.*
//import org.openapitools.server.api.model.*

val apiInstance = UserApi()
val user : kotlin.collections.List<User> =  // kotlin.collections.List<User> | List of user object
try {
    apiInstance.createUsersWithListInput(user)
} catch (e: ClientException) {
    println("4xx response calling UserApi#createUsersWithListInput")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UserApi#createUsersWithListInput")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**kotlin.collections.List&lt;User&gt;**](User.md)| List of user object |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: APPLICATION_JSON
 - **Accept**: Not defined

<a name="deleteUser"></a>
# **deleteUser**
> deleteUser(username)

Delete user

This can only be done by the logged in user.

### Example
```kotlin
// Import classes:
//import org.openapitools.infrastructure.*
//import org.openapitools.server.api.model.*

val apiInstance = UserApi()
val username : kotlin.String = username_example // kotlin.String | The name that needs to be deleted
try {
    apiInstance.deleteUser(username)
} catch (e: ClientException) {
    println("4xx response calling UserApi#deleteUser")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UserApi#deleteUser")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **kotlin.String**| The name that needs to be deleted |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getUserByName"></a>
# **getUserByName**
> User getUserByName(username)

Get user by user name



### Example
```kotlin
// Import classes:
//import org.openapitools.infrastructure.*
//import org.openapitools.server.api.model.*

val apiInstance = UserApi()
val username : kotlin.String = username_example // kotlin.String | The name that needs to be fetched. Use user1 for testing.
try {
    val result : User = apiInstance.getUserByName(username)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling UserApi#getUserByName")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UserApi#getUserByName")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **kotlin.String**| The name that needs to be fetched. Use user1 for testing. |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: APPLICATION_XML, APPLICATION_JSON

<a name="loginUser"></a>
# **loginUser**
> kotlin.String loginUser(username, password)

Logs user into the system



### Example
```kotlin
// Import classes:
//import org.openapitools.infrastructure.*
//import org.openapitools.server.api.model.*

val apiInstance = UserApi()
val username : kotlin.String = username_example // kotlin.String | The user name for login
val password : kotlin.String = password_example // kotlin.String | The password for login in clear text
try {
    val result : kotlin.String = apiInstance.loginUser(username, password)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling UserApi#loginUser")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UserApi#loginUser")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **kotlin.String**| The user name for login |
 **password** | **kotlin.String**| The password for login in clear text |

### Return type

**kotlin.String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: APPLICATION_XML, APPLICATION_JSON

<a name="logoutUser"></a>
# **logoutUser**
> logoutUser()

Logs out current logged in user session



### Example
```kotlin
// Import classes:
//import org.openapitools.infrastructure.*
//import org.openapitools.server.api.model.*

val apiInstance = UserApi()
try {
    apiInstance.logoutUser()
} catch (e: ClientException) {
    println("4xx response calling UserApi#logoutUser")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UserApi#logoutUser")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="updateUser"></a>
# **updateUser**
> updateUser(username, user)

Updated user

This can only be done by the logged in user.

### Example
```kotlin
// Import classes:
//import org.openapitools.infrastructure.*
//import org.openapitools.server.api.model.*

val apiInstance = UserApi()
val username : kotlin.String = username_example // kotlin.String | name that need to be deleted
val user : User =  // User | Updated user object
try {
    apiInstance.updateUser(username, user)
} catch (e: ClientException) {
    println("4xx response calling UserApi#updateUser")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling UserApi#updateUser")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **kotlin.String**| name that need to be deleted |
 **user** | [**User**](User.md)| Updated user object |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: APPLICATION_JSON
 - **Accept**: Not defined

