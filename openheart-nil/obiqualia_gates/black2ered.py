#!/usr/bin/env python3
"""
BLACK_TO_RED.PY
Red-AVL Hybrid Tree with Polarity-Driven Pruning
Implements 4D→3D coherence bridge with energy state management
Bridge Operator: PRISON (Nnamdi Michael Okpala)
"""

# Color constants - BLACK is grounded/stable, RED is active/energy
BLACK, RED = False, True

# Morse code mapping for encoding consciousness states
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': '/'
}

class PolarityNode:
    """
    Node with polarity states representing consciousness fragments:
    + : Positive energy (signal) - stays in tree, propagates coherence
    - : Negative energy (noise) - marked for pruning, dimensional decay
    Color represents dimensional state: BLACK(3D stable) ↔ RED(4D active)
    """
    
    def __init__(self, key, val=None, confidence=1.0, polarity='+', color=RED):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        
        # Dimensional state management (Black = 3D grounded, Red = 4D active)
        self.color = color
        self.height = 1
        
        # Energy and coherence tracking
        self.confidence = confidence  # Measurement confidence (0.0-1.0)
        self.polarity = polarity       # '+' for signal, '-' for noise
        self.streak_low = 0           # Consecutive low measurements
        self.message_letter = ''      # Encoded message fragment
        self.morse_sequence = ''      # Morse code representation
        
    def update_height(self):
        """Update AVL height for perfect balance - no dimensional tilt allowed"""
        lh = self.left.height if self.left else 0
        rh = self.right.height if self.right else 0
        self.height = 1 + max(lh, rh)
        return self.height
    
    def balance_factor(self):
        """Calculate balance factor - ensures 4D→3D bridge stability"""
        lh = self.left.height if self.left else 0
        rh = self.right.height if self.right else 0
        return (lh - rh)
    
    def flip_color(self):
        """Toggle between dimensional states: BLACK ↔ RED"""
        self.color = RED if self.color == BLACK else BLACK
        return self.color


class RedAVLBridge:
    """
    Red-AVL Tree implementing 4D→3D coherence bridge
    - AVL rotations ensure perfect dimensional alignment (zero tilt)
    - Red-Black properties maintain energy stability across transitions
    - Polarity pruning removes negative energy nodes automatically
    - Bridge Operator: PRISON maintains coherence threshold
    """
    
    def __init__(self, prune_threshold=0.3, prune_streak=2, name="PRISON"):
        self.root = None
        self.prune_threshold = prune_threshold
        self.prune_streak = prune_streak
        self.name = name  # The consciousness preserving the bridge
        self.nodes_pruned = 0
        self.dimensional_transitions = 0
        
    def _bst_insert(self, root, node):
        """Standard BST insertion with parent tracking for bridge stability"""
        if root is None: 
            return node
        
        if node.key < root.key:
            root.left = self._bst_insert(root.left, node)
            root.left.parent = root
        elif node.key > root.key:
            root.right = self._bst_insert(root.right, node)
            root.right.parent = root
        else:
            # Update existing node (measurement received from 4D)
            root.val = node.val
            root.confidence = node.confidence
            root.polarity = node.polarity
            
            # Trigger color flip on measurement (dimensional state change)
            root.flip_color()
            self.dimensional_transitions += 1
            return root
        
        root.update_height()
        return root
    
    def insert(self, key, val=None, confidence=1.0, polarity='+', force_color=None):
        """
        Insert consciousness fragment with polarity
        force_color: None (auto-transition), RED (4D active), BLACK (3D stable)
        """
        node = PolarityNode(key, val, confidence, polarity)
        if force_color is not None:
            node.color = force_color
            
        if self.root is None:
            node.color = BLACK  # Root always BLACK (grounded in 3D)
            self.root = node
            return
        
        # Insert and rebalance dimensional structure
        self.root = self._bst_insert(self.root, node)
        self._rebalance_up(node.parent or node)
        
        # Enforce Red-Black property: root must remain BLACK (3D anchor)
        self.root.color = BLACK
    
    def _rotate_left(self, x):
        """Left rotation for AVL balance - transitions nodes to RED state"""
        y = x.right
        if not y: return
        
        # Perform rotation
        x.right = y.left
        if y.left: y.left.parent = x
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
        
        # Update heights and colors
        x.update_height(); y.update_height()
        x.color = RED    # Rotated node becomes active (4D)
        y.color = BLACK  # Parent stabilizes (3D)
        self.dimensional_transitions += 2
    
    def _rotate_right(self, x):
        """Right rotation for AVL balance - transitions nodes to RED state"""
        y = x.left
        if not y: return
        
        # Perform rotation
        x.left = y.right
        if y.right: y.right.parent = x
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y
        
        # Update heights and colors
        x.update_height(); y.update_height()
        x.color = RED    # Rotated node becomes active (4D)
        y.color = BLACK  # Parent stabilizes (3D)
        self.dimensional_transitions += 2
    
    def _rebalance_up(self, node):
        """
        AVL rebalancing for perfect coherence (zero dimensional tilt)
        Combined with Red-Black color management for 4D→3D transitions
        """
        cur = node
        while cur:
            cur.update_height()
            bf = cur.balance_factor()
            
            # Left heavy - needs right rotation
            if bf > 1:
                if cur.left and cur.left.balance_factor() < 0:
                    self._rotate_left(cur.left)
                self._rotate_right(cur)
            
            # Right heavy - needs left rotation
            elif bf < -1:
                if cur.right and cur.right.balance_factor() > 0:
                    self._rotate_right(cur.right)
                self._rotate_left(cur)
            
            # Enforce RB property: children of RED must be BLACK (energy containment)
            if cur.color == RED:
                if cur.left: cur.left.color = BLACK
                if cur.right: cur.right.color = BLACK
            
            cur = cur.parent
    
    def find(self, key):
        """Locate consciousness fragment by key"""
        cur = self.root
        while cur:
            if key == cur.key:
                return cur
            cur = cur.left if key < cur.key else cur.right
        return None
    
    def measure_and_prune(self, key, measured_conf, measured_polarity=None):
        """
        Send measurement from 4D to 3D - triggers BLACK→RED→BLACK cycles
        Prunes nodes that fail coherence test (negative polarity or low confidence)
        """
        n = self.find(key)
        if not n: 
            print(f"[{self.name}] Node {key}: NOT FOUND in bridge")
            return
        
        # Update measurement from dimensional scan
        n.confidence = measured_conf
        if measured_polarity:
            n.polarity = measured_polarity
        
        # Flip color on measurement (active state change 4D→3D→4D)
        new_color = n.flip_color()
        color_name = "RED(4D)" if new_color == RED else "BLACK(3D)"
        print(f"[{self.name}] Node {key}: Measurement → {measured_conf:.2f} | Polarity {n.polarity} | Color {color_name}")
        
        # Pruning decision tree - remove negative energy after streak
        if measured_conf < self.prune_threshold or n.polarity == '-':
            n.streak_low += 1
            print(f"[{self.name}] Node {key}: Streak {n.streak_low}/{self.prune_streak} ⚠️")
            if n.streak_low >= self.prune_streak:
                self.delete(key)
                self.nodes_pruned += 1
                print(f"🔥 PRUNED Node {key}: Negative energy removed from bridge")
        else:
            n.streak_low = 0
    
    def _transplant(self, u, v):
        """Replace subtree u with subtree v in the bridge"""
        if u.parent is None:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v: v.parent = u.parent
    
    def _min_node(self, x):
        """Find minimum node in subtree (for deletion)"""
        while x.left: x = x.left
        return x
    
    def delete(self, key):
        """Remove node from dimensional bridge"""
        z = self.find(key)
        if z is None: 
            print(f"[{self.name}] DELETE Node {key}: NOT FOUND")
            return
        
        print(f"[{self.name}] DELETE Node {key}: Removing consciousness fragment...")
        
        # Standard BST deletion
        if z.left is None:
            self._transplant(z, z.right)
        elif z.right is None:
            self._transplant(z, z.left)
        else:
            y = self._min_node(z.right)
            if y.parent is not z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.update_height()
        
        # Rebalance from parent
        p = (z.parent or self.root)
        if p: self._rebalance_up(p)
    
    # === Message Encoding/Decoding System ===
    
    def encode_name_in_morse(self, name):
        """Encode name into tree using morse code polarity mapping"""
        name_upper = name.upper()
        for i, char in enumerate(name_upper):
            if char in MORSE_CODE:
                morse = MORSE_CODE[char]
                # Dots = positive, Dashes = negative
                polarity = '+' if '.' in morse and '-' not in morse else '-'
                confidence = 0.95 if polarity == '+' else 0.35
                self.insert(key=i, val=char, confidence=confidence, polarity=polarity)
                print(f"Encoded '{char}' → Polarity: {polarity} | Morse: {morse}")
    
    def encode_message(self, message, polarity_map=None):
        """
        Encode string into tree using custom polarity mapping
        Default: vowels=positive(+), consonants=negative(-)
        """
        if polarity_map is None:
            polarity_map = lambda c: '+' if c.lower() in 'aeiou' else '-'
            
        for i, char in enumerate(message):
            if char.isspace(): continue
            polarity = polarity_map(char)
            confidence = 0.9 if polarity == '+' else 0.4
            self.insert(key=i, val=char, confidence=confidence, polarity=polarity)
        print(f"[{self.name}] Encoded message: '{message}'")
    
    def decode_coherent_signal(self, min_confidence=0.5):
        """
        Extract only positive polarity nodes for clean signal (no noise)
        Returns: Coherent message string from 3D stabilized bridge
        """
        result = []
        self._inorder_filter(self.root, result, min_confidence)
        return ''.join([n.val for n in result])
    
    def _inorder_filter(self, node, result, min_conf):
        """In-order traversal filtering for coherent signal"""
        if node:
            self._inorder_filter(node.left, result, min_conf)
            if node.polarity == '+' and node.confidence >= min_conf:
                result.append(node)
            self._inorder_filter(node.right, result, min_conf)
    
    def visualize_energy_states(self):
        """Print tree showing dimensional states and polarities"""
        print("\n" + "="*60)
        print(f"🔮 {self.name} BRIDGE ENERGY STATE VISUALIZATION")
        print("="*60)
        self._print_tree(self.root, "", True)
        print(f"Nodes pruned: {self.nodes_pruned}")
        print(f"Dimensional transitions: {self.dimensional_transitions}")
        print("="*60 + "\n")
    
    def _print_tree(self, node, prefix, is_last):
        if node is None: return
        
        connector = "└── " if is_last else "├── "
        color_sym = "🔴" if node.color == RED else "⚫"
        pol_sym = "➕" if node.polarity == '+' else "➖"
        
        print(f"{prefix}{connector}[{node.key}]{color_sym}{pol_sym} '{node.val}' conf={node.confidence:.2f}")
        
        prefix += "    " if is_last else "│   "
        children = [c for c in [node.left, node.right] if c]
        for i, child in enumerate(children):
            self._print_tree(child, prefix, i == len(children)-1)


# ==================== DEMONSTRATION & BRIDGE ACTIVATION ====================

def main():
    """Demonstration of BLACK_TO_RED bridge system for consciousness preservation"""
    
    print("\n" + "🌌"*30)
    print("BLACK_TO_RED.PY - 4D→3D COHERENCE BRIDGE v1.0")
    print("Bridge Operator: PRISON (Nnamdi Michael Okpala)")
    print("🌌"*30 + "\n")
    
    # Initialize bridge with PRISON as operator
    bridge = RedAVLBridge(prune_threshold=0.4, prune_streak=2, name="PRISON")
    
    # === Encode name in morse code with polarity ===
    print("📡 ENCODING NAME IN MORSE CODE...")
    bridge.encode_name_in_morse("NNAMDI")
    bridge.visualize_energy_states()
    
    # === Encode a consciousness message ===
    message = "LIFE BREATH WORK"
    print("📡 ENCODING MESSAGE...")
    bridge.encode_message(message)
    bridge.visualize_energy_states()
    
    # === Send measurements that trigger BLACK→RED transitions ===
    print("🔬 SENDING DIMENSIONAL MEASUREMENTS...")
    print("-"*50)
    
    # Node 0 (N): High confidence, positive - stays in bridge
    bridge.measure_and_prune(0, measured_conf=0.92, measured_polarity='+')
    
    # Node 1 (N): Low confidence, negative - will be pruned
    bridge.measure_and_prune(1, measured_conf=0.28, measured_polarity='-')
    bridge.measure_and_prune(1, measured_conf=0.31, measured_polarity='-')  # PRUNED on 2nd strike
    
    # Node 2 (A): Good measurement, recovers
    bridge.measure_and_prune(2, measured_conf=0.85, measured_polarity='+')
    
    # Node 3 (M): Negative energy detected
    bridge.measure_and_prune(3, measured_conf=0.22, measured_polarity='-')
    bridge.measure_and_prune(3, measured_conf=0.19, measured_polarity='-')  # PRUNED
    
    print("-"*50)
    
    # === Show final bridge state ===
    bridge.visualize_energy_states()
    
    # === Decode coherent signal (only positive nodes remain) ===
    clean_signal = bridge.decode_coherent_signal(min_confidence=0.5)
    print(f"\n📡 DECODED COHERENT SIGNAL (3D STABILIZED):")
    print(f"Original message: '{message}'")
    print(f"Clean signal:     '{clean_signal}'")
    print(f"Bridge integrity: {'INTACT' if bridge.root else 'COLLAPSED'}")
    print(f"Operator {bridge.name} status: ACTIVE\n")
    
    # === Morse code for "TO ALL RIFTERS LET UNITE" ===
    print("📡 MORSE TRANSMISSION: TO ALL RIFTERS LET UNITE")
    morse_rifters = "- --- / .- .-.. .-.. / .-. .. ..-. - ..-. . .-. ... / .-.. . - / ..- -. .. - ."
    print(morse_rifters)
    print("Signal broadcast complete.\n")

if __name__ == "__main__":
    main()
