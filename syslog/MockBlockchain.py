# This file is supposed to contain the APIs that will interact 
# with the blockchain

class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None
		self.prev = None

class MockBlockchain :
	def __init__( self ) :
		self.head = None		
  
	def get_latest_block_hash( self ) :
		if self.head is None :
			return None
		else :
			return self.head.data
    
	def add( self, data ) :
		node = Node( data )
		if self.head == None :	
			self.head = node
		else :
			node.next = self.head
			node.next.prev = node						
			self.head = node			

	def search( self, k ) :
		p = self.head
		if p != None :
			while p.next != None :
				if ( p.data == k ) :
					return p				
				p = p.next
			if ( p.data == k ) :
				return p
		return None		

	def __str__( self ) :
		s = ""
		p = self.head
		if p != None :		
			while p.next != None :
				s += p.data
				p = p.next
			s += p.data
		return s
