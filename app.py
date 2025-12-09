from flask import Flask, render_template, request, jsonify
import json
import re
import os
from groq import Groq

app = Flask(__name__)

# Initialize Groq client
# Get API key from environment variable
GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

class RequirementsAnalyzer:
    def __init__(self):
        self.keywords = {
            'data_storage': ['store', 'save', 'database', 'persist', 'record'],
            'authentication': ['login', 'signup', 'register', 'authenticate', 'user'],
            'api': ['api', 'endpoint', 'rest', 'interface'],
            'ui': ['display', 'show', 'view', 'interface', 'dashboard'],
            'processing': ['process', 'calculate', 'compute', 'analyze'],
            'notification': ['notify', 'alert', 'email', 'send'],
            'search': ['search', 'find', 'query', 'filter'],
            'payment': ['payment', 'checkout', 'transaction', 'purchase']
        }
    
    def analyze_with_groq(self, requirement):
        """Use Groq LLM for advanced analysis"""
        if not groq_client:
            return None
        
        try:
            prompt = f"""You are a senior software architect. Analyze the following business requirement and provide a detailed technical breakdown.

Business Requirement:
{requirement}

Provide your analysis in the following JSON format:
{{
    "modules": ["list of system modules like authentication, data_storage, api, ui, etc."],
    "entities": ["list of data entities/models like User, Product, Order, etc."],
    "relationships": ["describe relationships between entities"],
    "technical_considerations": ["security concerns", "scalability needs", "performance requirements"],
    "recommended_architecture": "brief architecture description"
}}

Be specific and comprehensive. Focus on technical accuracy."""

            response = groq_client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert software architect specializing in system design and technical specifications. Always respond with valid JSON."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.3,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content
            # Extract JSON from response
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            if json_start != -1 and json_end > json_start:
                json_str = content[json_start:json_end]
                return json.loads(json_str)
            return None
            
        except Exception as e:
            print(f"Groq API Error: {str(e)}")
            return None
    
    def generate_schema_with_groq(self, entities, modules, requirement):
        """Generate database schemas using Groq"""
        if not groq_client:
            return self.generate_schema_fallback(entities, modules)
        
        try:
            prompt = f"""Based on this requirement: "{requirement}"

Generate database schemas for these entities: {', '.join(entities)}
Context modules: {', '.join(modules)}

For each entity, provide a SQL schema with:
- Appropriate fields based on the business requirement
- Correct data types
- Proper constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL)
- Relationships between tables

Respond in JSON format:
{{
    "EntityName": {{
        "table_name": "table_name",
        "fields": [
            {{"name": "field_name", "type": "data_type", "constraints": "constraints"}},
            ...
        ],
        "relationships": ["description of foreign keys and relationships"]
    }}
}}"""

            response = groq_client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a database architect expert. Design optimal database schemas with proper normalization."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.2,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            if json_start != -1 and json_end > json_start:
                json_str = content[json_start:json_end]
                return json.loads(json_str)
            return self.generate_schema_fallback(entities, modules)
            
        except Exception as e:
            print(f"Schema Generation Error: {str(e)}")
            return self.generate_schema_fallback(entities, modules)
    
    def generate_pseudocode_with_groq(self, modules, entities, requirement):
        """Generate pseudocode using Groq"""
        if not groq_client:
            return self.generate_pseudocode_fallback(modules, entities)
        
        try:
            prompt = f"""Based on this requirement: "{requirement}"

Generate detailed pseudocode for the main functionalities.
Modules involved: {', '.join(modules)}
Entities: {', '.join(entities)}

For each major functionality, provide:
1. Function name
2. Step-by-step pseudocode with proper logic flow
3. Error handling
4. Edge cases consideration

Respond in JSON format:
{{
    "functions": [
        {{
            "function": "function_name",
            "description": "what this function does",
            "code": "detailed pseudocode here"
        }}
    ]
}}

Make the pseudocode clear, logical, and production-ready."""

            response = groq_client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert programmer who writes clear, efficient pseudocode for system implementations."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.3,
                max_tokens=3000
            )
            
            content = response.choices[0].message.content
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            if json_start != -1 and json_end > json_start:
                json_str = content[json_start:json_end]
                data = json.loads(json_str)
                return data.get('functions', [])
            return self.generate_pseudocode_fallback(modules, entities)
            
        except Exception as e:
            print(f"Pseudocode Generation Error: {str(e)}")
            return self.generate_pseudocode_fallback(modules, entities)
    
    def generate_architecture_with_groq(self, modules, requirement):
        """Generate system architecture using Groq"""
        if not groq_client:
            return self.generate_architecture_fallback(modules)
        
        try:
            prompt = f"""Based on this requirement: "{requirement}"

Design a complete system architecture.
Identified modules: {', '.join(modules)}

Provide:
1. Architecture layers (Frontend, Backend, Database, etc.)
2. Recommended technologies for each layer
3. Communication patterns (REST API, WebSockets, etc.)
4. Deployment considerations
5. Security measures
6. Scalability approach

Respond in JSON format:
{{
    "layers": ["layer names"],
    "technologies": {{
        "frontend": ["tech1", "tech2"],
        "backend": ["tech1", "tech2"],
        "database": ["tech1", "tech2"]
    }},
    "patterns": ["architecture patterns being used"],
    "security": ["security measures"],
    "scalability": "scalability approach description"
}}"""

            response = groq_client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a solutions architect expert in designing scalable, secure system architectures."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.3,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            if json_start != -1 and json_end > json_start:
                json_str = content[json_start:json_end]
                return json.loads(json_str)
            return self.generate_architecture_fallback(modules)
            
        except Exception as e:
            print(f"Architecture Generation Error: {str(e)}")
            return self.generate_architecture_fallback(modules)
    
    # Fallback methods (original rule-based logic)
    def extract_modules_fallback(self, requirement):
        """Fallback module extraction"""
        modules = []
        requirement_lower = requirement.lower()
        
        for module_type, keywords in self.keywords.items():
            if any(keyword in requirement_lower for keyword in keywords):
                modules.append(module_type)
        
        words = requirement.split()
        entities = [word.strip('.,!?') for word in words 
                   if word and word[0].isupper() and len(word) > 3]
        
        return list(set(modules)), list(set(entities))
    
    def generate_schema_fallback(self, entities, modules):
        """Fallback schema generation"""
        schemas = {}
        
        for entity in entities:
            schema = {
                'table_name': entity.lower() + 's',
                'fields': [
                    {'name': 'id', 'type': 'INTEGER', 'constraints': 'PRIMARY KEY AUTO_INCREMENT'},
                    {'name': 'created_at', 'type': 'TIMESTAMP', 'constraints': 'DEFAULT CURRENT_TIMESTAMP'}
                ]
            }
            
            if 'authentication' in modules:
                if 'user' in entity.lower():
                    schema['fields'].extend([
                        {'name': 'email', 'type': 'VARCHAR(255)', 'constraints': 'UNIQUE NOT NULL'},
                        {'name': 'password_hash', 'type': 'VARCHAR(255)', 'constraints': 'NOT NULL'},
                        {'name': 'username', 'type': 'VARCHAR(100)', 'constraints': 'UNIQUE NOT NULL'}
                    ])
            
            if 'data_storage' in modules:
                schema['fields'].extend([
                    {'name': 'name', 'type': 'VARCHAR(255)', 'constraints': 'NOT NULL'},
                    {'name': 'description', 'type': 'TEXT', 'constraints': 'NULL'},
                    {'name': 'status', 'type': 'VARCHAR(50)', 'constraints': 'DEFAULT "active"'}
                ])
            
            schemas[entity] = schema
        
        return schemas
    
    def generate_pseudocode_fallback(self, modules, entities):
        """Fallback pseudocode generation"""
        pseudocode = []
        
        if 'authentication' in modules:
            pseudocode.append({
                'function': 'user_registration',
                'description': 'Handle user registration with validation',
                'code': '''FUNCTION register_user(email, password, username):
    VALIDATE email format
    VALIDATE password strength (min 8 chars)
    CHECK if email already exists in database
    IF email exists:
        RETURN error "Email already registered"
    
    hash_password = HASH(password)
    user_id = INSERT INTO users (email, password_hash, username)
    RETURN success with user_id
END FUNCTION'''
            })
        
        if 'data_storage' in modules and entities:
            entity = entities[0]
            pseudocode.append({
                'function': f'create_{entity.lower()}',
                'description': f'Create new {entity} record',
                'code': f'''FUNCTION create_{entity.lower()}(data):
    VALIDATE required fields in data
    IF validation fails:
        RETURN error "Missing required fields"
    
    {entity.lower()}_id = INSERT INTO {entity.lower()}s (data)
    RETURN success with {entity.lower()}_id
END FUNCTION'''
            })
        
        return pseudocode
    
    def generate_architecture_fallback(self, modules):
        """Fallback architecture generation"""
        architecture = {
            'layers': [],
            'technologies': {}
        }
        
        if 'ui' in modules or any(m in modules for m in ['authentication', 'data_storage']):
            architecture['layers'].append('Presentation Layer (Frontend)')
            architecture['technologies']['frontend'] = ['HTML5', 'CSS3', 'JavaScript', 'React/Vue.js']
        
        if any(m in modules for m in ['api', 'processing', 'authentication']):
            architecture['layers'].append('Business Logic Layer (Backend)')
            architecture['technologies']['backend'] = ['Python/Flask', 'Node.js/Express', 'Java/Spring Boot']
        
        if 'data_storage' in modules:
            architecture['layers'].append('Data Access Layer')
            architecture['technologies']['database'] = ['PostgreSQL', 'MySQL', 'MongoDB']
        
        return architecture

analyzer = RequirementsAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        requirement = data.get('requirement', '')
        
        if not requirement:
            return jsonify({'error': 'No requirement provided'}), 400
        
        # Check if Groq is available
        use_groq = groq_client is not None
        
        if use_groq:
            # Use Groq LLM for analysis
            llm_analysis = analyzer.analyze_with_groq(requirement)
            
            if llm_analysis:
                modules = llm_analysis.get('modules', [])
                entities = llm_analysis.get('entities', [])
                
                # Generate schemas with Groq
                schemas = analyzer.generate_schema_with_groq(entities, modules, requirement)
                
                # Generate pseudocode with Groq
                pseudocode = analyzer.generate_pseudocode_with_groq(modules, entities, requirement)
                
                # Generate architecture with Groq
                architecture = analyzer.generate_architecture_with_groq(modules, requirement)
                
                result = {
                    'modules': modules,
                    'entities': entities,
                    'schemas': schemas,
                    'pseudocode': pseudocode,
                    'architecture': architecture,
                    'llm_insights': {
                        'relationships': llm_analysis.get('relationships', []),
                        'technical_considerations': llm_analysis.get('technical_considerations', []),
                        'recommended_architecture': llm_analysis.get('recommended_architecture', '')
                    },
                    'powered_by': 'Groq LLM (Llama 3.3 70B)'
                }
                
                return jsonify(result)
        
        # Fallback to rule-based analysis
        modules, entities = analyzer.extract_modules_fallback(requirement)
        schemas = analyzer.generate_schema_fallback(entities, modules)
        pseudocode = analyzer.generate_pseudocode_fallback(modules, entities)
        architecture = analyzer.generate_architecture_fallback(modules)
        
        result = {
            'modules': modules,
            'entities': entities,
            'schemas': schemas,
            'pseudocode': pseudocode,
            'architecture': architecture,
            'powered_by': 'Rule-Based Analysis (Groq API key not configured)'
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'groq_available': groq_client is not None
    })

if __name__ == '__main__':
    if not GROQ_API_KEY:
        print("WARNING: GROQ_API_KEY not found in environment variables")
        print("Set it with: export GROQ_API_KEY='your-api-key-here'")
        print("Using fallback rule-based analysis\n")
    else:
        print("Groq API configured successfully\n")
    
    app.run(debug=True, port=5000)