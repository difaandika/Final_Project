describe('Final Project', () => {
  it('Add attachment on my info',() => {
    cy.visit('https://opensource-demo.orangehrmlive.com/')
    cy.get("input[placeholder='Username']").type('Admin')
    cy.get("input[placeholder='Password']").type('admin123')
    cy.get("button[type='submit']").click()
    cy.get(".oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module").should('contain', 'Dashboard')
    cy.get("body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(6) > a:nth-child(1)").click()
    cy.get("button[class='oxd-button oxd-button--medium oxd-button--text']").click()
    cy.get(".oxd-file-button").click()
    cy.get("div[class='orangehrm-attachment'] button[type='submit']").click()
  })
})