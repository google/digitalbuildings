package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Field 
* The class of all fields
*/
@SuppressWarnings("serial")
public class Field implements IField{

	IRI newInstance;
	public Field(String namespace, String instanceId) {		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Field"));
	}

	public IRI iri()
	{
		return newInstance;
	}


	public void setTimeSeriesId(String param)
	{
	 GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasTimeSeriesId"), GLOBAL.factory.createLiteral(param));
	}

	public String getTimeSeriesId(){
		return (GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasTimeSeriesId"), null).objects().iterator().next()).stringValue();
	}
	@java.lang.Override
	public String stringValue() {
		return this.newInstance.getLocalName();
	}

	@java.lang.Override
	public String getNamespace() {
		return this.newInstance.getNamespace();
	}

	@java.lang.Override
	public String getLocalName() {
		return this.newInstance.getLocalName();
	}

	@java.lang.Override
	public String toString() {
		return this.newInstance.toString();
	}

	public static Set<IField> getAllFieldsObjectsCreated(){
		Set<IField> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Field")).subjects().stream()
		.map(mapper->(IField)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}