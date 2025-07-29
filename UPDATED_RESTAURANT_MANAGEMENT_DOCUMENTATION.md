# Django Restaurant Management System - Updated Documentation

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Core Features](#core-features)
4. [User Interface Design](#user-interface-design)
5. [Screen Designs](#screen-designs)
6. [Database Models](#database-models)
7. [Django Implementation](#django-implementation)
8. [Installation & Setup](#installation--setup)
9. [Theme & Styling](#theme--styling)

---

## 🎯 Project Overview

Django Restaurant Management System with Material UI 7 design language, featuring a clean Google Sites-inspired interface. The system provides role-based access for waiters, kitchen staff, and administrators with real-time order management and inventory tracking.

### Core Objectives
- **Clean Interface**: Google Sites-inspired Material UI 7 design
- **Responsive Design**: Bootstrap-powered responsive layouts
- **Role-based Access**: Secure user authentication and permissions
- **Real-time Updates**: WebSocket-based live notifications
- **Professional Theme**: Both light and dark mode support

---

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 4.2+
- **Database**: MySQL 8.0+
- **Real-time**: Django Channels (WebSocket)
- **Authentication**: Django's built-in auth system

### Frontend
- **Languages**: HTML5, CSS3, JavaScript (ES6+)
- **CSS Framework**: Bootstrap 5.3+
- **Design System**: Material UI 7
- **Theme**: Google Sites inspired
- **Icons**: Material Design Icons
- **Fonts**: Google Fonts (Roboto, Inter)

### No APIs Required
- Server-side rendering with Django templates
- HTMX for dynamic updates (optional)
- WebSocket for real-time features

---

## 🚀 Core Features

### 👨‍🍳 Waiter Interface
- Clean table management dashboard
- Intuitive order placement system
- Real-time order status tracking
- Payment processing interface
- Customer management

### 🔪 Kitchen Interface
- Order queue management
- Status update system (Pending → In Progress → Complete)
- Timer-based order tracking
- Multi-chef collaboration
- Audio/visual notifications

### 🛠️ Admin Interface
- Inventory management system
- Menu item administration
- User management
- Sales analytics dashboard
- System settings

### 📊 Features
- Light/Dark mode toggle
- Responsive design for all devices
- Real-time notifications
- Print-friendly order receipts
- Daily/weekly reports

---

## 🎨 User Interface Design

### Design Principles
- **Material UI 7**: Latest Material Design guidelines
- **Google Sites Aesthetic**: Clean, professional, minimal
- **Accessibility**: WCAG 2.1 AA compliant
- **Consistency**: Uniform spacing, typography, colors
- **Navigation**: Simple, intuitive menu structures

### Color Scheme

#### Light Mode
```css
Primary: #1976D2 (Blue)
Secondary: #424242 (Dark Grey)
Surface: #FFFFFF (White)
Background: #F5F5F5 (Light Grey)
Text Primary: #212121 (Dark Grey)
Text Secondary: #757575 (Medium Grey)
Success: #4CAF50 (Green)
Warning: #FF9800 (Orange)
Error: #F44336 (Red)
```

#### Dark Mode
```css
Primary: #2196F3 (Light Blue)
Secondary: #90A4AE (Blue Grey)
Surface: #121212 (Dark Surface)
Background: #000000 (Black)
Text Primary: #FFFFFF (White)
Text Secondary: #B0BEC5 (Light Grey)
Success: #66BB6A (Light Green)
Warning: #FFB74D (Light Orange)
Error: #EF5350 (Light Red)
```

---

## 📱 Screen Designs

### 1. Login Screen

```
┌─────────────────────────────────────────────────────────────┐
│                    Restaurant Manager                      │
│                                                             │
│    ┌─────────────────────────────────────────────────┐    │
│    │                                                 │    │
│    │           🍽️ RestaurantPOS                      │    │
│    │                                                 │    │
│    │     ┌─────────────────────────────────────┐     │    │
│    │     │ Username                            │     │    │
│    │     │ [                               ]   │     │    │
│    │     └─────────────────────────────────────┘     │    │
│    │                                                 │    │
│    │     ┌─────────────────────────────────────┐     │    │
│    │     │ Password                            │     │    │
│    │     │ [                               ]   │     │    │
│    │     └─────────────────────────────────────┘     │    │
│    │                                                 │    │
│    │     ┌─────────────────────────────────────┐     │    │
│    │     │           SIGN IN                   │     │    │
│    │     └─────────────────────────────────────┘     │    │
│    │                                                 │    │
│    │           [🌙 Dark Mode Toggle]                 │    │
│    │                                                 │    │
│    └─────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2. Waiter Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│ ☰ Restaurant POS    👤 John Doe (Waiter)    🔔[3] 🌙 ⚙️ 🚪 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Dashboard > Tables                                          │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Table Management                                       │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│ │  Table 1 │ │  Table 2 │ │  Table 3 │ │  Table 4 │        │
│ │    🟢    │ │    🔴    │ │    🟡    │ │    ⚪    │        │
│ │  Available│ │ Occupied │ │ Pending  │ │ Reserved │        │
│ │  4 seats  │ │  2/4     │ │  3/6     │ │  8 seats │        │
│ │          │ │  25 min  │ │  10 min  │ │          │        │
│ │ [SELECT] │ │ [VIEW]   │ │ [VIEW]   │ │ [SETUP]  │        │
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘        │
│                                                             │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│ │  Table 5 │ │  Table 6 │ │  Table 7 │ │  Table 8 │        │
│ │    🟢    │ │    🔴    │ │    🟢    │ │    🟡    │        │
│ │  Available│ │ Occupied │ │ Available│ │ Cleaning │        │
│ │  2 seats  │ │  1/2     │ │  6 seats │ │  4 seats │        │
│ │          │ │  45 min  │ │          │ │          │        │
│ │ [SELECT] │ │ [VIEW]   │ │ [SELECT] │ │ [CLEAN]  │        │
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘        │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Recent Orders                                           │ │
│ │ ┌─────────────────────────────────────────────────────┐ │ │
│ │ │ #001 | Table 2 | 🟡 In Progress | $45.20 | 25 min  │ │ │
│ │ │ #002 | Table 6 | 🟢 Ready       | $23.50 | Serve!  │ │ │
│ │ │ #003 | Table 5 | 🔴 Pending     | $67.80 | 2 min   │ │ │
│ │ └─────────────────────────────────────────────────────┘ │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3. Order Taking Screen

```
┌─────────────────────────────────────────────────────────────┐
│ ☰ Restaurant POS    👤 John Doe    🔔[3] 🌙 ⚙️ 🚪          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Dashboard > Tables > Table 1 > New Order                   │
│                                                             │
│ ┌─────────────────────┐ ┌─────────────────────────────────┐ │
│ │ Order Details       │ │ Menu Categories                 │ │
│ │                     │ │                                 │ │
│ │ Table: 1            │ │ [🍽️ Appetizers] [🍝 Main Course] │ │
│ │ Guests: 4           │ │ [🍰 Desserts]   [🥤 Beverages]   │ │
│ │ Waiter: John Doe    │ │                                 │ │
│ │ Time: 14:25         │ │ ┌─────────────────────────────┐ │ │
│ │                     │ │ │ Main Course                 │ │ │
│ │ Current Order:      │ │ │                             │ │ │
│ │                     │ │ │ ┌─────────────────────────┐ │ │ │
│ │ ┌─────────────────┐ │ │ │ │ 🍕 Margherita Pizza     │ │ │ │
│ │ │ • Pizza x2 $30  │ │ │ │ │ Fresh tomato, mozzarella│ │ │ │
│ │ │ • Salad x1 $12  │ │ │ │ │ $15.99 | ⏱️ 20 min      │ │ │ │
│ │ │ • Coke  x4 $16  │ │ │ │ │ [➕ ADD TO ORDER]       │ │ │ │
│ │ └─────────────────┘ │ │ │ └─────────────────────────┘ │ │ │
│ │                     │ │ │                             │ │ │
│ │ Subtotal: $58.00    │ │ │ ┌─────────────────────────┐ │ │ │
│ │ Tax: $4.64          │ │ │ │ 🍝 Pasta Carbonara      │ │ │ │
│ │ Total: $62.64       │ │ │ │ Creamy bacon pasta      │ │ │ │
│ │                     │ │ │ │ $18.99 | ⏱️ 15 min      │ │ │ │
│ │ [📝 PLACE ORDER]    │ │ │ │ [➕ ADD TO ORDER]       │ │ │ │
│ │ [🗑️ CLEAR]          │ │ │ └─────────────────────────┘ │ │ │
│ └─────────────────────┘ │ └─────────────────────────────┘ │ │
│                         └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### 4. Kitchen Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│ ☰ Kitchen Dashboard  👤 Chef Maria    🔔[5] 🌙 ⚙️ 🚪       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Kitchen > Order Queue                                       │
│                                                             │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│ │🆕 NEW (3)   │ │📋 PROGRESS  │ │✅ READY (2)  │            │
│ │             │ │    (4)      │ │             │            │
│ └─────────────┘ └─────────────┘ └─────────────┘            │
│                                                             │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│ │ Order #001  │ │ Order #002  │ │ Order #004  │            │
│ │ Table: 1    │ │ Table: 3    │ │ Table: 2    │            │
│ │ Guests: 4   │ │ Guests: 2   │ │ Guests: 3   │            │
│ │ ⏱️ Just now  │ │ ⏱️ 15 min   │ │ ⏱️ 28 min   │            │
│ │             │ │             │ │             │            │
│ │ Items:      │ │ Items:      │ │ Items:      │            │
│ │ • 2x Pizza  │ │ • 1x Pasta  │ │ • 3x Burger │            │
│ │ • 1x Salad  │ │ • 2x Soup   │ │ • 2x Fries  │            │
│ │ • 4x Coke   │ │ • 1x Bread  │ │ • 1x Shake  │            │
│ │             │ │             │ │             │            │
│ │ [🟢 START]  │ │ [✅ DONE]   │ │ [📞 NOTIFY] │            │
│ │ [❌ REJECT] │ │ [⏸️ PAUSE]  │ │ [🔄 REFIRE] │            │
│ └─────────────┘ └─────────────┘ └─────────────┘            │
│                                                             │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│ │ Order #005  │ │ Order #003  │ │ Order #006  │            │
│ │ Table: 5    │ │ Table: 4    │ │ Table: 6    │            │
│ │ Guests: 2   │ │ Guests: 6   │ │ Guests: 2   │            │
│ │ ⏱️ 2 min    │ │ ⏱️ 22 min   │ │ ⏱️ 35 min   │            │
│ │             │ │             │ │             │            │
│ │ Items:      │ │ Items:      │ │ Items:      │            │
│ │ • 1x Steak  │ │ • 2x Fish   │ │ • 1x Salad  │            │
│ │ • 2x Wine   │ │ • 1x Rice   │ │ • 1x Water  │            │
│ │             │ │ • 3x Juice  │ │             │            │
│ │             │ │             │ │             │            │
│ │ [🟢 START]  │ │ [✅ DONE]   │ │ [📞 NOTIFY] │            │
│ │ [❌ REJECT] │ │ [⏸️ PAUSE]  │ │ [🔄 REFIRE] │            │
│ └─────────────┘ └─────────────┘ └─────────────┘            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 5. Admin Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│ ☰ Admin Panel    👤 Admin User    🔔[2] 🌙 ⚙️ 🚪           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Admin > Dashboard                                           │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Today's Overview - January 15, 2024                    │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐      │
│ │ 💰 Revenue    │ │ 📋 Orders     │ │ 👥 Customers  │      │
│ │               │ │               │ │               │      │
│ │   $2,450.00   │ │      87       │ │     145       │      │
│ │   ↑ +12.5%    │ │   ↑ +8.2%     │ │   ↑ +15.3%   │      │
│ └───────────────┘ └───────────────┘ └───────────────┘      │
│                                                             │
│ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐      │
│ │ 🍽️ Avg Order  │ │ ⏰ Peak Hour   │ │ 📊 Top Dish   │      │
│ │               │ │               │ │               │      │
│ │    $28.16     │ │   7:00-8:00   │ │ Margherita    │      │
│ │   ↑ +2.1%     │ │      PM       │ │    Pizza      │      │
│ └───────────────┘ └───────────────┘ └───────────────┘      │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Quick Actions                                           │ │
│ │                                                         │ │
│ │ [👥 Manage Users] [🍽️ Menu Items] [📦 Inventory]       │ │
│ │ [📈 Reports] [⚙️ Settings] [🔔 Notifications]          │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ ⚠️ Alerts & Notifications                               │ │
│ │                                                         │ │
│ │ • 🔴 Low Stock: Tomatoes (5 kg remaining)               │ │
│ │ • 🟡 Order #1241 taking longer than expected (45 min)  │ │
│ │ • 🔵 New user registration pending approval             │ │
│ │ • 🟢 Daily backup completed successfully               │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 6. Inventory Management

```
┌─────────────────────────────────────────────────────────────┐
│ ☰ Admin Panel    👤 Admin User    🔔[2] 🌙 ⚙️ 🚪           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Admin > Inventory Management                                │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Inventory Overview                                      │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Search: [🔍 ingredient name...] [🟢 In Stock ▼] [Add+] │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Ingredient   │Current│ Min │ Unit │ Status  │ Action    │ │
│ ├─────────────┼───────┼─────┼──────┼─────────┼───────────┤ │
│ │ Tomatoes    │15.5kg │ 10kg│  kg  │🟢 Good  │[📝 Edit]  │ │
│ │ Flour       │ 8.2kg │ 15kg│  kg  │🟡 Low   │[📝 Edit]  │ │
│ │ Mozzarella  │ 3.1kg │  5kg│  kg  │🔴 Critical│[📝 Edit]│ │
│ │ Olive Oil   │ 2.8L  │  2L │  L   │🟢 Good  │[📝 Edit]  │ │
│ │ Chicken     │12.5kg │  8kg│  kg  │🟢 Good  │[📝 Edit]  │ │
│ │ Pasta       │ 4.2kg │  6kg│  kg  │🟡 Low   │[📝 Edit]  │ │
│ │ Rice        │18.7kg │ 10kg│  kg  │🟢 Good  │[📝 Edit]  │ │
│ │ Onions      │ 6.3kg │  5kg│  kg  │🟢 Good  │[📝 Edit]  │ │
│ └─────────────┴───────┴─────┴──────┴─────────┴───────────┘ │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ [➕ Add New Ingredient] [📊 Usage Report] [🔄 Refresh] │ │
│ │ [📦 Bulk Import] [📋 Export CSV] [⚠️ Alert Settings]   │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 7. Payment Processing

```
┌─────────────────────────────────────────────────────────────┐
│ ☰ Restaurant POS    👤 John Doe    🔔[3] 🌙 ⚙️ 🚪          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Dashboard > Tables > Table 1 > Payment                     │
│                                                             │
│ ┌─────────────────────┐ ┌─────────────────────────────────┐ │
│ │ Order Summary       │ │ Payment Processing              │ │
│ │                     │ │                                 │ │
│ │ Order #001          │ │ ┌─────────────────────────────┐ │ │
│ │ Table: 1            │ │ │ Payment Method              │ │ │
│ │ Guests: 4           │ │ │                             │ │ │
│ │ Waiter: John Doe    │ │ │ [💳 Card] [💵 Cash] [📱 Digital] │ │ │
│ │                     │ │ └─────────────────────────────┘ │ │
│ │ Items:              │ │                                 │ │ │
│ │ • 2x Pizza    $30.00│ │ ┌─────────────────────────────┐ │ │
│ │ • 1x Salad    $12.00│ │ │ Bill Breakdown              │ │ │
│ │ • 4x Coke     $16.00│ │ │                             │ │ │
│ │                     │ │ │ Subtotal:      $58.00       │ │ │
│ │ Subtotal:    $58.00 │ │ │ Tax (8%):       $4.64       │ │ │
│ │ Tax (8%):     $4.64 │ │ │ Tip:           $8.00       │ │ │
│ │ Tip:          $8.00 │ │ │ ─────────────────────        │ │ │
│ │ ─────────────────── │ │ │ Total:         $70.64       │ │ │
│ │ TOTAL:       $70.64 │ │ └─────────────────────────────┘ │ │
│ │                     │ │                                 │ │ │
│ │ [🖨️ Print Receipt] │ │ ┌─────────────────────────────┐ │ │
│ │ [📧 Email Receipt]  │ │ │ Amount Paid: $ [         ]  │ │ │
│ └─────────────────────┘ │ │ Change Due:  $ 0.00         │ │ │
│                         │ │                             │ │ │
│                         │ │ [💰 PROCESS PAYMENT]        │ │ │
│                         │ │ [🔙 BACK TO ORDER]          │ │ │
│                         │ └─────────────────────────────┘ │ │
│                         └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗄️ Database Models (MySQL)

### User Management
```python
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('waiter', 'Waiter'),
        ('chef', 'Chef'),
        ('admin', 'Administrator'),
        ('manager', 'Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True)
    is_active_session = models.BooleanField(default=False)
    theme_preference = models.CharField(max_length=10, default='light')
    created_at = models.DateTimeField(auto_now_add=True)
```

### Restaurant Structure
```python
class Table(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('reserved', 'Reserved'),
        ('cleaning', 'Cleaning'),
    ]
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    current_guests = models.IntegerField(default=0)
    last_cleaned = models.DateTimeField(null=True, blank=True)
```

### Menu Management
```python
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)  # Material icon name
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.IntegerField()  # minutes
    image = models.ImageField(upload_to='menu/', blank=True)
    is_available = models.BooleanField(default=True)
    ingredients = models.TextField()  # JSON field for ingredients
```

### Order System
```python
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('ready', 'Ready'),
        ('served', 'Served'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]
    
    order_number = models.CharField(max_length=20, unique=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    waiter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    guest_count = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    special_instructions = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='pending')
```

---

## ⚙️ Django Implementation

### Settings Configuration
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'restaurant_management',
        'USER': 'restaurant_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Local apps
    'accounts',
    'restaurant',
    'orders',
    'inventory',
    'analytics',
    
    # Third party
    'channels',
]

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# WebSocket
ASGI_APPLICATION = 'restaurant_management.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

### URL Configuration
```python
# urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('orders/', include('orders.urls')),
    path('tables/', include('restaurant.urls')),
    path('inventory/', include('inventory.urls')),
    path('analytics/', include('analytics.urls')),
]
```

### Views Structure
```python
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    if request.user.role == 'waiter':
        return render(request, 'waiter/dashboard.html')
    elif request.user.role == 'chef':
        return render(request, 'kitchen/dashboard.html')
    elif request.user.role == 'admin':
        return render(request, 'admin/dashboard.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')
```

---

## 🎨 Theme & Styling

### Bootstrap + Material UI 7 Integration

```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurant Management System</title>
    
    <!-- Bootstrap 5.3 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Material Design Icons -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    
    <!-- Custom CSS -->
    <link href="{% static 'css/material-theme.css' %}" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <span class="material-icons">restaurant</span>
                RestaurantPOS
            </a>
            
            <div class="d-flex align-items-center">
                <button class="btn btn-outline-secondary me-2" onclick="toggleTheme()">
                    <span class="material-icons" id="theme-icon">dark_mode</span>
                </button>
                <div class="dropdown">
                    <button class="btn btn-outline-primary dropdown-toggle" type="button" data-bs-toggle="dropdown">
                        <span class="material-icons">account_circle</span>
                        {{ user.get_full_name|default:user.username }}
                    </button>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#">Settings</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="container-fluid py-4">
        {% block content %}
        {% endblock %}
    </main>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- Custom JS -->
    <script src="{% static 'js/theme-toggle.js' %}"></script>
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>
```

### Custom CSS (Material Theme)
```css
/* static/css/material-theme.css */
:root {
  /* Light Theme */
  --md-primary: #1976D2;
  --md-primary-variant: #1565C0;
  --md-secondary: #424242;
  --md-background: #F5F5F5;
  --md-surface: #FFFFFF;
  --md-error: #F44336;
  --md-success: #4CAF50;
  --md-warning: #FF9800;
  --md-on-primary: #FFFFFF;
  --md-on-surface: #212121;
  --md-on-background: #212121;
}

[data-theme="dark"] {
  /* Dark Theme */
  --md-primary: #2196F3;
  --md-primary-variant: #1976D2;
  --md-secondary: #90A4AE;
  --md-background: #121212;
  --md-surface: #1E1E1E;
  --md-error: #EF5350;
  --md-success: #66BB6A;
  --md-warning: #FFB74D;
  --md-on-primary: #000000;
  --md-on-surface: #FFFFFF;
  --md-on-background: #FFFFFF;
}

/* Global Styles */
body {
  font-family: 'Roboto', sans-serif;
  background-color: var(--md-background);
  color: var(--md-on-background);
  transition: all 0.3s ease;
}

/* Material Cards */
.card {
  background-color: var(--md-surface);
  border: none;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
}

.card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.15);
  transform: translateY(-2px);
}

/* Material Buttons */
.btn-primary {
  background-color: var(--md-primary);
  border-color: var(--md-primary);
  border-radius: 8px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn-primary:hover {
  background-color: var(--md-primary-variant);
  border-color: var(--md-primary-variant);
}

/* Table Status Indicators */
.table-card {
  transition: all 0.3s ease;
  cursor: pointer;
}

.table-card.available {
  border-left: 4px solid var(--md-success);
}

.table-card.occupied {
  border-left: 4px solid var(--md-error);
}

.table-card.reserved {
  border-left: 4px solid var(--md-warning);
}

/* Order Status Pills */
.order-status {
  padding: 4px 12px;
  border-radius: 16px;
  font-size: 0.875rem;
  font-weight: 500;
}

.status-pending {
  background-color: #FFF3E0;
  color: #E65100;
}

.status-progress {
  background-color: #E3F2FD;
  color: #0277BD;
}

.status-ready {
  background-color: #E8F5E8;
  color: #2E7D32;
}

/* Navigation */
.navbar {
  background-color: var(--md-surface) !important;
  border-bottom: 1px solid rgba(0,0,0,0.1);
}

[data-theme="dark"] .navbar {
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

/* Form Inputs */
.form-control {
  border-radius: 8px;
  border: 1px solid #E0E0E0;
  transition: all 0.3s ease;
}

.form-control:focus {
  border-color: var(--md-primary);
  box-shadow: 0 0 0 0.2rem rgba(25, 118, 210, 0.25);
}

/* Loading States */
.loading {
  position: relative;
  overflow: hidden;
}

.loading::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
  animation: loading 1.5s infinite;
}

@keyframes loading {
  0% { left: -100%; }
  100% { left: 100%; }
}
```

### Theme Toggle JavaScript
```javascript
// static/js/theme-toggle.js
function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    html.setAttribute('data-theme', newTheme);
    
    // Update icon
    const icon = document.getElementById('theme-icon');
    icon.textContent = newTheme === 'dark' ? 'light_mode' : 'dark_mode';
    
    // Save preference
    localStorage.setItem('theme', newTheme);
    
    // Send to server
    fetch('/api/theme/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({theme: newTheme})
    });
}

// Load saved theme
document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    const icon = document.getElementById('theme-icon');
    if (icon) {
        icon.textContent = savedTheme === 'dark' ? 'light_mode' : 'dark_mode';
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
```

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.9+
- MySQL 8.0+
- Node.js (for frontend build tools)

### Step-by-Step Installation

```bash
# 1. Clone repository
git clone <repository-url>
cd restaurant-management

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install Python dependencies
pip install Django mysqlclient channels channels-redis Pillow

# 4. Create MySQL database
mysql -u root -p
CREATE DATABASE restaurant_management CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'restaurant_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON restaurant_management.* TO 'restaurant_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# 5. Configure Django settings
cp settings.py.example settings.py
# Edit database credentials in settings.py

# 6. Run migrations
python manage.py makemigrations
python manage.py migrate

# 7. Create superuser
python manage.py createsuperuser

# 8. Collect static files
python manage.py collectstatic

# 9. Run development server
python manage.py runserver
```

This updated documentation reflects your requirements for a clean, Google Sites-inspired Material UI 7 theme with Django backend, HTML/CSS/JS frontend, Bootstrap framework, and MySQL database - no APIs needed!