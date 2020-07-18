package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_occupancy_status;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_occupancy_status;

/**
* Class Fan_us_svl_brg1_1 
* Non-standard type for BRG1
*/
@SuppressWarnings("serial")
public class Fan_us_svl_brg1_1 extends www.google.com.digitalbuildings._0_0_1.hvac.Fan_ss implements IFan_us_svl_brg1_1{

	IRI newInstance;
	public Fan_us_svl_brg1_1(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_svl_brg1_1"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesZone_occupancy_status (IZone_occupancy_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_occupancy_status> getUsesZone_occupancy_status (){
		Set<IZone_occupancy_status> UsesZone_occupancy_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_occupancy_status) {
				UsesZone_occupancy_status.add((Zone_occupancy_status)action);
			}
		});
		return UsesZone_occupancy_status;
	}

	public static Set<IFan_us_svl_brg1_1> getAllFan_us_svl_brg1_1sObjectsCreated(){
		Set<IFan_us_svl_brg1_1> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_svl_brg1_1")).subjects().stream()
		.map(mapper->(IFan_us_svl_brg1_1)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}