# ProcrastiKiller - Gamified Productivity App

A full-featured web application that transforms productivity into an epic gaming experience. Complete tasks, earn rewards, battle monsters, and build your arsenal of weapons!

## 🌟 Features

### Core Gameplay
- **Task Management**: Create and complete tasks with time-based rewards
- **Gamified Rewards**: Earn coins and XP based on time spent on tasks
- **Weapon Gacha System**: Pull weapons with varying rarities and damage
- **Monster Battles**: Fight monsters using XP and earn coin rewards
- **Weapon Crafting**: Merge duplicate weapons to increase damage
- **Profile System**: Track your progress, level, and achievements

### Website Structure
- **Landing Page** (`index.html`): Marketing site with features and call-to-action
- **Main App** (`app.html`): Full game interface with all features
- **About Page** (`about.html`): Company story and mission
- **Contact Page** (`contact.html`): Contact form and support information
- **Help Center** (`help.html`): Comprehensive guides and troubleshooting
- **Legal Pages**: Terms of Service, Privacy Policy, and more

## 🎮 How to Play

### Getting Started
1. **Create Tasks**: Add your daily tasks in the Tasks tab
2. **Complete Tasks**: Take your time - longer tasks earn more rewards!
3. **Earn Rewards**: Get coins and XP based on time spent (5-60 minutes)
4. **Pull Weapons**: Use 100 coins to pull weapons from the gacha
5. **Battle Monsters**: Spend XP to attack monsters and earn coins
6. **Craft Weapons**: Merge duplicate weapons to increase damage

### Reward System
- **Coins**: 0-60 coins based on task duration (5-60 minutes)
- **XP**: 10-120 XP based on task duration (5-60 minutes)
- **Leveling**: Every 100 XP increases your level

### Weapon System
- **Rarities**: Common, Rare, Epic, Legendary
- **Damage Range**: 10-100 damage
- **Crafting**: Merge same weapons for +0.5% damage increase

### Battle System
- **Monsters**: 5 different types with increasing difficulty
- **Attack Cost**: XP cost varies by monster difficulty
- **Rewards**: Coin rewards based on monster strength

## 🏗️ Technical Details

### Technology Stack
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Storage**: Browser localStorage for data persistence
- **Design**: Responsive design with modern CSS Grid and Flexbox
- **Animations**: CSS transitions and keyframe animations

### File Structure
```
app dev/
├── index.html          # Landing page
├── app.html           # Main game application
├── about.html         # About page
├── contact.html       # Contact page
├── help.html          # Help center
├── terms.html         # Terms of service
├── privacy.html       # Privacy policy
└── README.md          # This file
```

### Key Features
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Local Storage**: Game progress saved automatically
- **Cross-Browser Compatible**: Works in all modern browsers
- **No Server Required**: Runs entirely in the browser
- **Privacy-First**: No personal data collected or transmitted

## 🚀 Getting Started

1. **Download/Clone** the project files
2. **Open** `index.html` in your web browser
3. **Navigate** to the "Play Now" section or open `app.html` directly
4. **Start Playing** by creating your first task!

## 🎯 Game Mechanics

### Task Completion Rewards
| Time Spent | Coins | XP |
|------------|-------|----|
| 0-5 min    | 0     | 10 |
| 5-10 min   | 5     | 20 |
| 10-15 min  | 10    | 30 |
| ...        | ...   | ...|
| 55-60 min  | 60    | 120|

### Monster Stats
| Monster     | HP  | Damage | XP Cost | Coin Reward |
|-------------|-----|--------|---------|-------------|
| Goblin      | 50  | 10     | 5       | 20          |
| Orc         | 100 | 20     | 10      | 40          |
| Troll       | 200 | 35     | 20      | 80          |
| Dragon      | 500 | 80     | 50      | 200         |
| Demon Lord  | 1000| 150    | 100     | 500         |

### Weapon Rarities
| Rarity      | Drop Rate | Weapons |
|-------------|-----------|---------|
| Common      | 80%       | Wooden Sword, Iron Sword |
| Rare        | 15%       | Steel Sword |
| Epic        | 4%        | Magic Staff |
| Legendary   | 1%        | Dragon Blade |

## 🛠️ Customization

### Adding New Features
- **New Weapons**: Add to the `weapons` array in `app.html`
- **New Monsters**: Add to the `monsters` array in `app.html`
- **New Pages**: Create new HTML files and link them in navigation
- **Styling**: Modify CSS in the `<style>` sections

### Data Persistence
Game data is stored in browser localStorage with the key `'procrastikiller'`. The data structure includes:
- Player level, XP, and coins
- Task list with completion status
- Weapon inventory
- Monsters defeated
- Crafting slots

## 🐛 Troubleshooting

### Common Issues
1. **Progress Lost**: Check if localStorage is enabled in your browser
2. **Weapons Not Appearing**: Ensure you have enough coins (100 per pull)
3. **Monsters Not Spawning**: Wait a few minutes or refresh the page
4. **Tasks Not Completing**: Try refreshing the page

### Browser Compatibility
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 📱 Mobile Support

The application is fully responsive and optimized for mobile devices:
- Touch-friendly interface
- Optimized layouts for small screens
- Swipe gestures supported
- Mobile-optimized navigation

## 🔒 Privacy & Security

- **No Personal Data**: We don't collect or store personal information
- **Local Storage**: All game data stays on your device
- **No Tracking**: No analytics or tracking cookies
- **Open Source**: Transparent code for security review

## 🤝 Contributing

This is a demonstration project. Feel free to:
- Fork and modify for your own use
- Report bugs or suggest features
- Share with others who might find it useful

## 📄 License

This project is open source and available under the MIT License.

## 🎉 Credits

Created as a demonstration of gamified productivity concepts. Built with modern web technologies and designed for maximum user engagement.

---

**Ready to level up your productivity? Start your epic journey with ProcrastiKiller today!** ⚔️🎮
