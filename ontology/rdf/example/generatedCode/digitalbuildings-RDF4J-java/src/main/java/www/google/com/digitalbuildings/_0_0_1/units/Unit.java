package www.google.com.digitalbuildings._0_0_1.units;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Unit 
* Class of all units
*/
@SuppressWarnings("serial")
public class Unit implements IUnit{

	IRI newInstance;
	public Unit(String namespace, String instanceId) {		super();
		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Unit"));
	}

	public IRI iri()
	{
		return newInstance;
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

	public static Set<IUnit> getAllUnitsObjectsCreated(){
		Set<IUnit> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Unit")).subjects().stream()
		.map(mapper->(IUnit)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}