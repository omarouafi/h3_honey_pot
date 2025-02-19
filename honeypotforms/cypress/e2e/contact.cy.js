// filepath: /C:/Users/Cloud/Documents/h3hitema/h3_honey_pot/honeypotforms/src/app/page.test.js
describe('Home Page Form', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('should submit the form successfully with valid data', () => {
      cy.get('input[name="name"]').type('John Doe');
      cy.get('input[name="email"]').type('john.doe@example.com');
      cy.get('textarea[name="message"]').type('This is a test message.');
      cy.get('button[type="submit"]').click();
      cy.get('.text-green-500').should('contain', 'Form submitted successfully!');
    });
  
    it('should detect bot when honeypot field is filled', () => {
      cy.get('input[name="name"]').type('John Doe');
      cy.get('input[name="email"]').type('john.doe@example.com');
      cy.get('textarea[name="message"]').type('This is a test message.');
      cy.get('input[name="honeypot"]').type('bot');
      cy.get('button[type="submit"]').click();
      cy.get('.text-red-500').should('contain', 'Bot detected!');
    });
  
  
  });